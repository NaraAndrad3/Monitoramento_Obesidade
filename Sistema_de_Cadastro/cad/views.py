from django.shortcuts import render
from .models import Usuario # se models está na mesma pasta que views, tem que usar .models
import joblib

# Create your views here.

def home(request):
    return render(request, 'usuarios/home.html')

knn_model = joblib.load('/home/nara/Documentos/2024.1/SistemasInteligentes/pythonProjects/Sistema_de_Cadastro/machine/knn.pkl')

def usuarios(request):
    print('entrou aqui')
    if request.method == 'POST':
        novo_usuario = Usuario()
        # Extraí as informações da tela e coloca dentro de um novo usuário
        novo_usuario.genero = request.POST.get('genero')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.altura = request.POST.get('altura')
        novo_usuario.peso = request.POST.get('peso')
        novo_usuario.family_history = request.POST.get('family')
        novo_usuario.FAVC = request.POST.get('FAVC')
        novo_usuario.FCVC = request.POST.get('FCVC')
        novo_usuario.NCP = request.POST.get('NCP')
        novo_usuario.CAEC = request.POST.get('CAEC')
        novo_usuario.SMOKE = request.POST.get('SMOKE')
        novo_usuario.CH2O = request.POST.get('CH2O')
        novo_usuario.SCC = request.POST.get('SCC')
        novo_usuario.FAF = request.POST.get('FAF')
        novo_usuario.TUE = request.POST.get('TUE')
        novo_usuario.CALC = request.POST.get('CALC')
        novo_usuario.MTrans = request.POST.get('MTRANS')
        
        print('entrou aqui também')
        print('genero:', novo_usuario.genero)
        print('idade:', novo_usuario.idade)
        print('altura:', novo_usuario.altura)
        print('peso:', novo_usuario.peso)
        print('family_history:', novo_usuario.family_history)
        print('FAVC:', novo_usuario.FAVC)
        print('FCVC:', novo_usuario.FCVC)
        print('NCP:', novo_usuario.NCP)
        print('CAEC:', novo_usuario.CAEC)
        print('SMOKE:', novo_usuario.SMOKE)
        print('CH2O:', novo_usuario.CH2O)
        print('SCC:', novo_usuario.SCC)
        print('FAF:', novo_usuario.FAF)
        print('TUE:', novo_usuario.TUE)
        print('CALC:', novo_usuario.CALC)
        print('MTrans:', novo_usuario.MTrans)
        
        features = [
            
            novo_usuario.idade,
            novo_usuario.altura,
            novo_usuario.peso,
            novo_usuario.FCVC,
            novo_usuario.NCP,
            novo_usuario.CH2O,
            novo_usuario.FAF,
            novo_usuario.TUE,
            novo_usuario.genero,
            novo_usuario.family_history,
            novo_usuario.FAVC,  
            novo_usuario.CAEC,
            novo_usuario.SMOKE,
            novo_usuario.SCC,
            novo_usuario.CALC,
            novo_usuario.MTrans,
             
        ]
        
        # Age 	Height 	Weight 	FCVC 	NCP 	CH2O 	FAF 	TUE 	genero 	family 	FAVC 	CAEC 	SMOKE 	SCC 	CALC 	MTRANS
        print('Features before conversion:', features)
        
        try:
            features = [float(f) if not isinstance(f, (int, float)) else f for f in features]
        except ValueError as e:
            print('Error in feature conversion:', e)
            return render(request, 'usuarios/usuarios.html', {'mensagem': 'Erro na conversão dos dados.'})
        
        print('Features after conversion:', features)
        
        try:
            pred = knn_model.predict([features])[0]
        except Exception as e:
            print('Error in prediction:', e)
            return render(request, 'usuarios/usuarios.html', {'mensagem': 'Erro ao fazer a predição.'})
        
        print('Predição:', pred)
        novo_usuario.NObeyesdad = pred
        
        prediction_map = {
            0: 'Insufficient_Weight',
            1: 'Normal_Weight',
            2: 'Obesity_Type_I',
            3: 'Obesity_Type_II',
            4: 'Obesity_Type_III',
            5: 'Overweight_Level_I',
            6: 'Overweight_Level_II'
        }

        mensagem = prediction_map.get(pred, "Unknown_Category")
        
        novo_usuario.save()
        
        return render(request, 'usuarios/usuarios.html', {'mensagem': mensagem})
    else:
        return render(request, 'usuarios/usuarios.html')
