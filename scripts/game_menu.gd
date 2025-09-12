
extends Control

func _on_company_button_pressed() -> void:
	$click_sound.play()

func _on_back_button_pressed() -> void:
	$click_sound.play()
	await $click_sound.finished
	get_tree().change_scene_to_file("res://scenes/main_menu.tscn")
