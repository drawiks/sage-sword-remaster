
class_name weaponManager
extends Node

var _weapon: Weapon

func _init() -> void:
	_weapon = preload("res://resources/weapon.tres").duplicate()

func add_damage(amount: float) -> void:
	_weapon.weapon_damage += amount

func add_upgrade_cost() -> void:
	_weapon.weapon_upgrade_cost += 100

func get_data() -> Array:
	return [_weapon.weapon_damage, _weapon.weapon_upgrade_cost]
