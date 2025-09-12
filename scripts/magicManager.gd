
class_name magicManager
extends Node

var _magic: Magic

func _init() -> void:
	_magic = preload("res://resources/magic.tres").duplicate()

func add_damage(amount: float) -> void:
	_magic.damage += amount

func add_upgrade_cost() -> void:
	_magic.upgrade_cost += 100

func get_data() -> Dictionary:
	return {
		"damage":_magic.damage,
		"upgrade_cost":_magic.upgrade_cost
	}
