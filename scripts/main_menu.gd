
extends Control

func _ready() -> void:
	AudioManager.play_audio(preload("res://assets/sounds/menu.mp3"))

func _on_play_button_pressed() -> void:
	if !$click_sound.playing:
		$click_sound.play()
	
func _on_shop_button_pressed() -> void:
	$click_sound.play()
	await $click_sound.finished
	get_tree().change_scene_to_file("res://scenes/shop_menu.tscn")
	
func _on_quit_button_pressed() -> void:
	$click_sound.play()
	await  $click_sound.finished
	get_tree().quit()
