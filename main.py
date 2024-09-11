import os
import random
import pandas as pd
import torch
import torchaudio
from audiomentations import Compose, PitchShift, TimeStretch, Gain, Shift


torch.manual_seed(42)
random.seed(42)

#path
input_dir = "voice-data/en/clips"
output_dir = "augmented_common_voice"
metadata_file = "augmentation_metadata.csv"

# Create output folder
os.makedirs(output_dir, exist_ok=True)

# Define augmentation techniques
augmentations = Compose([
    PitchShift(min_semitones=-4, max_semitones=4, p=0.5),
    TimeStretch(min_rate=0.8, max_rate=1.2, p=0.5),
    Gain(min_gain_in_db=-6, max_gain_in_db=6, p=0.5),
    Shift(min_shift=-0.5, max_shift=0.5, p=0.5),
])

def apply_augmentations(audio, sample_rate):
    augmented = augmentations(samples=audio.numpy(), sample_rate=sample_rate)
    return torch.from_numpy(augmented)


def add_noise(audio, noise_level=0.005):
    noise = torch.randn_like(audio) * noise_level
    return audio + noise

# Process audio files
metadata = []

for filename in os.listdir(input_dir):
    if filename.endswith(".mp3"):
        input_path = os.path.join(input_dir, filename)
        
        # Load audio file
        audio, sample_rate = torchaudio.load(input_path)
        
        # Apply augmentations
        augmented_audio = apply_augmentations(audio, sample_rate)
        
        # Add noise (simulating background noise)
        if random.random() < 0.5:
            augmented_audio = add_noise(augmented_audio)
        
        # Generate output filename
        output_filename = f"aug_{filename}"
        output_path = os.path.join(output_dir, output_filename)
        
        # Save augmented audio
        torchaudio.save(output_path, augmented_audio, sample_rate)
        
        # Record metadata
        applied_augmentations = [aug.__class__.__name__ for aug in augmentations.transforms if random.random() < aug.p]
        if random.random() < 0.5:
            applied_augmentations.append("AddNoise")
        metadata.append({
            "original_file": filename,
            "augmented_file": output_filename,
            "augmentations": ", ".join(applied_augmentations)
        })

metadata_df = pd.DataFrame(metadata)
metadata_df.to_csv(metadata_file, index=False)

print(f"Augmentation complete. Augmented files saved in {output_dir}")
print(f"Metadata saved to {metadata_file}")