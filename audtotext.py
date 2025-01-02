import torchaudio
import torch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load the pretrained Wav2Vec 2.0 model
bundle = torchaudio.pipelines.WAV2VEC2_ASR_BASE_960H
model = bundle.get_model().to(device)
labels = bundle.get_labels()
# Load the audio file
waveform, sample_rate = torchaudio.load(r'C:\Users\saini\PycharmProjects\PythonProject2\Data\audio3.wav')

# Resample if necessary
if sample_rate != bundle.sample_rate:
    waveform = torchaudio.functional.resample(waveform, sample_rate, bundle.sample_rate)
waveform = waveform.to(device)

# Perform inference
with torch.inference_mode():
    emissions, _ = model(waveform)

# Decode the emissions to text
def greedy_decoder(emissions, labels):
    # Get the index of the highest probability for each frame
    predicted_ids = torch.argmax(emissions, dim=-1)

    # Collapse repeated ids and remove blanks (assuming blank id is 0)
    collapsed_ids = torch.unique_consecutive(predicted_ids, dim=-1)
    non_blank_ids = [id for id in collapsed_ids if id != 0]

    # Convert ids to corresponding labels
    transcription = ''.join([labels[id] for id in non_blank_ids])
    return transcription

# Decode the emissions
transcription = greedy_decoder(emissions[0], labels)
print("Transcription:", transcription)






