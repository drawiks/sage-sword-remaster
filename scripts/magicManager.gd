
class_name magicManager
extends Node

var _magic: Magic

func _init() -> void:
	_magic = preload("res://resources/magic.tres").duplicate()

func add_damage(amount: float) -> void:
	_magic.weapon_damage += amount

func add_upgrade_cost() -> void:
	_magic.weapon_upgrade_cost += 100

func get_data() -> Array:
	return [_magic.magic_damage, _magic.magic_upgrade_cost]
