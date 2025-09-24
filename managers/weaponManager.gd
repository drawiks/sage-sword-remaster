
class_name weaponManager
extends Node

var _weapon: Weapon

func _init() -> void:
	_weapon = preload("res://resources/weapon.tres").duplicate()

func add_damage(amount: float) -> void:
	_weapon.damage += amount

func add_crit_chance(amount: float) -> void:
	_weapon.crit_chance += amount

func add_upgrade_cost() -> void:
	_weapon.upgrade_cost += 200

func get_data() -> Dictionary:
	return {
		"damage":_weapon.damage,
		"upgrade_cost":_weapon.upgrade_cost,
		"crit_chance":_weapon.crit_chance
	}

func calculate_damage(damage: int, crit_chance: float, crit_multiplier: float = 1.8) -> int:
	var roll = randf_range(0.0, 100.0)
	if roll < crit_chance:
		return int(damage * crit_multiplier)
	return damage
