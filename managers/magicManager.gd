
class_name magicManager
extends Node

var _magic: Magic

func _init() -> void:
	_magic = preload("res://resources/magic.tres").duplicate()

func add_damage(amount: float) -> void:
	_magic.damage += amount

func add_upgrade_cost() -> void:
	_magic.upgrade_cost += 200

func get_data() -> Dictionary:
	return {
		"damage":_magic.damage,
		"upgrade_cost":_magic.upgrade_cost
	}

func calculate_damage() -> float:
	var roll = randf_range(0.0, 100.0)
	if roll < _magic.chance:
		return _magic.damage * 1.8
	return 0.0
