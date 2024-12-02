import os
from pydub import AudioSegment

def convert_ckd_to_ogg(input_file, output_file):
    """
    Converte um arquivo .wav.ckd para .ogg.
    
    Args:
        input_file (str): Caminho do arquivo .wav.ckd de entrada.
        output_file (str): Caminho do arquivo .ogg de saída.
    """
    try:
        # Lê o conteúdo do arquivo CKD como WAV
        if not input_file.endswith('.wav.ckd'):
            raise ValueError("O arquivo deve ter a extensão .wav.ckd.")
        
        # Extração direta do conteúdo do .ckd
        temp_wav = input_file.replace('.ckd', '_temp.wav')
        with open(input_file, 'rb') as ckd_file:
            wav_data = ckd_file.read()
        
        # Salva o conteúdo temporariamente como .wav
        with open(temp_wav, 'wb') as wav_file:
            wav_file.write(wav_data)

        # Converte o arquivo WAV para OGG
        audio = AudioSegment.from_file(temp_wav, format="wav")
        audio.export(output_file, format="ogg")
        
        print(f"Arquivo convertido com sucesso: {output_file}")

        # Remove arquivo temporário
        os.remove(temp_wav)

    except Exception as e:
        print(f"Erro durante a conversão: {e}")

# Execução principal do script com tratamento para evitar fechamento automático
try:
    input_ckd = "exemplo.wav.ckd"
    output_ogg = "exemplo.ogg"
    convert_ckd_to_ogg(input_ckd, output_ogg)
except Exception as e:
    print(f"Erro inesperado: {e}")
finally:
    # Pausa no final para evitar fechamento automático
    input("\nPressione Enter para sair...")

