
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googletrans import Translator

def (texto):
    
    tradutor = Translator()
    texto_traduzido = tradutor.translate(texto, dest='en').text
    
    # Realiza a análise de sentimentos com VADER
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(texto_traduzido)
    
    compound = scores['compound']
    
    if compound >= 0.6:
        return "Muito positivo 😄 (Entusiasmado/Euforia)"
    elif compound >= 0.2:
        return "Positivo 🙂 (Contentamento/Otimismo)"
    elif compound <= -0.6:
        return "Muito negativo 😠 (Raiva/Ódio)"
    elif compound <= -0.2:
        return "Negativo 🙁 (Tristeza/Desânimo)"
    else:
        return "Neutro 😐 (Neutro/Equilibrado)"

frase = input("Digite uma frase para análise de emoção: ").strip()

if frase:
    emocao = analisar_emocao(frase)
    print("\n" + "="*70)
    print(f"Frase original: {frase}")
    print(f"Emoção detectada: {emocao}")
    print("="*70)

else:
    print("Por favor, digite uma frase válida.")