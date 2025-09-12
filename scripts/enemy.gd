
extends Node2D

@onready var sprite: AnimatedSprite2D = $sprite
@onready var timer: Timer = $timer
@onready var sound: AudioStreamPlayer2D = $audio

@export var enemy: Enemy
var weapon: Dictionary

var hit: bool = true

func _ready() -> void:
	weapon = WeaponManager.get_data()
	
	$game_over_panel.visible = false
	
	$enemy_health_bar.visible = true
	$area.visible = true
	sprite.visible = true
	
	enemy = preload("res://resources/enemy.tres").duplicate()
	sprite.play("idle")

func _process(delta: float) -> void:
	$enemy_health_bar.text = "♡ %.1f" % enemy.health

func _on_area_input_event(viewport: Node, event: InputEvent, shape_idx: int) -> void:
	if event is InputEventMouseButton and event.button_index == MOUSE_BUTTON_LEFT and event.pressed:
		if hit:
			hit = false
			
			enemy.health -= WeaponManager.calculate_damage(weapon.damage, weapon.crit_chance)
			
			if enemy.health <= 0:
				$enemy_health_bar.visible = false
				if sprite.animation != "die":
					sprite.play("die")
			else:
				if sprite.animation != "hurt":
					sprite.play("hurt")
			
			sound.play()
			timer.start(0.45)

func _on_sprite_animation_finished() -> void:
	if sprite.animation == "hurt":
		sprite.play("idle")
	elif sprite.animation == "die":
		sprite.visible = false
		$area.visible = false
		$game_over_panel.visible = true

func _on_timer_timeout() -> void:
	hit = true
