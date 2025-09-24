
class_name pointsManager
extends Node

var _points: Points
var points: float

func _init() -> void:
	_points = preload("res://resources/points.tres").duplicate()
	points = _points.points

func earn_points(amount: float) -> void:
	points += amount

func spend_points(amount: float) -> bool:
	if points >= amount:
		points -= amount
		return true
	else:
		return false

func get_points() -> float:
	return points
