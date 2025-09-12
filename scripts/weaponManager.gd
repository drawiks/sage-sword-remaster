
class_name weaponManager
extends Node

var _weapon: Weapon

func _init() -> void:
	_weapon = preload("res://resources/weapon.tres").duplicate()

func add_damage(amount: float) -> void:
	_weapon.damage += amount

func add_upgrade_cost() -> void:
	_weapon.upgrade_cost += 100

func get_data() -> Dictionary:
	return {
		"damage":_weapon.damage,
		"upgrade_cost":_weapon.upgrade_cost
	}
