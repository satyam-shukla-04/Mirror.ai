from services.voice_analyzer import analyze_voice

profile = analyze_voice(
    "../uploads/audio/voice_reference.wav"
)

print(profile)