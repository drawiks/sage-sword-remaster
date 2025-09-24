
extends Node2D

var enemy_level: int

func _ready() -> void:
	enemy_level = EnemyManager.get_level()
	
	$level.text = "LEVEL: %d" % enemy_level
	
	$cave_background.visible = false
	$golem_blue.visible = false
	$golem_gold.visible = false
	
	if enemy_level <= 10:
		$cave_background.visible = true
		$golem_blue.visible = true
	elif enemy_level <= 20 and enemy_level >= 10:
		$cave_background.visible = true
		$golem_gold.visible = true
