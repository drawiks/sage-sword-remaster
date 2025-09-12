
extends Node

var player: AudioStreamPlayer

func _ready():
	player = AudioStreamPlayer.new()
	add_child(player)

func play_audio(stream: AudioStream):
	if player.playing:
		return
	else:
		player.stream = stream
		player.play()

func stop_audio():
	player.stop()
