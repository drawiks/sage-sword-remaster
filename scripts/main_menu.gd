
extends Control

func _ready() -> void:
	AudioManager.play_audio(preload("res://assets/sounds/menu.mp3"))
	
	$panel/play_button.disabled = false
	$panel/shop_button.disabled = false

func _on_play_button_pressed() -> void:
	$panel/play_button.disabled = true
	
	$click_sound.play()
	await $click_sound.finished
	
	get_tree().change_scene_to_file("res://scenes/game_menu.tscn")
	
func _on_shop_button_pressed() -> void:
	$panel/shop_button.disabled = true
	
	$click_sound.play()
	await $click_sound.finished
	
	get_tree().change_scene_to_file("res://scenes/shop_menu.tscn")
	
func _on_quit_button_pressed() -> void:
	$click_sound.play()
	await  $click_sound.finished
	get_tree().quit()
