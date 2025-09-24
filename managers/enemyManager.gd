
class_name enemyManager
extends Node

var _enemy: Enemy

func _init() -> void:
	_enemy = preload("res://resources/enemy.tres").duplicate()

func add_health() -> void:
	_enemy.health += 500

func add_level() -> void:
	_enemy.level += 1

func get_health() -> float:
	return _enemy.health

func get_level() -> int:
	return _enemy.level
