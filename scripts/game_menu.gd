
extends Control

func _ready() -> void:
	$panel/company_button.disabled = false

func _on_company_button_pressed() -> void:
	$panel/company_button.disabled = true
	
	$click_sound.play()
	await $click_sound.finished
	
	get_tree().change_scene_to_file("res://scenes/company.tscn")

func _on_back_button_pressed() -> void:
	$click_sound.play()
	await $click_sound.finished
	get_tree().change_scene_to_file("res://scenes/main_menu.tscn")
