
extends Node2D

@onready var sprite: AnimatedSprite2D = $sprite
@onready var sound: AudioStreamPlayer2D = $audio
@onready var timer: Timer = $timer

@onready var crit_label = $crit_label
@onready var crit_timer = $crit_timer

@onready var magic_label = $magic_label
@onready var magic_timer = $magic_timer

var health: float

var weapon: Dictionary
var magic: Dictionary

var hit: bool = true

func _ready() -> void:
	weapon = WeaponManager.get_data()
	magic = MagicManager.get_data()
	
	$game_over_panel.visible = false
	
	$enemy_health_bar.visible = true
	$area.visible = true
	sprite.visible = true
	
	health = EnemyManager.get_health()
	sprite.play("idle")
	

@warning_ignore("unused_parameter")
func _process(delta: float) -> void:
	$enemy_health_bar.text = "♡ %.1f" % health

func show_crit(damage: float):
	crit_label.text = "CRIT! %.1f" % damage
	crit_label.visible = true
	crit_timer.start(0.5)

func show_magic(damage: float):
	magic_label.text = "MAGIC!!! %.1f" % damage
	magic_label.visible = true
	magic_timer.start(0.6)

func _on_area_input_event(_viewport: Node, event: InputEvent, _shape_idx: int) -> void:
	if event is InputEventMouseButton and event.button_index == MOUSE_BUTTON_LEFT and event.pressed:
		if hit:
			hit = false
			
			var damage = WeaponManager.calculate_damage(weapon.damage, weapon.crit_chance)
			if damage != weapon.damage:
				show_crit(damage)
				health -= damage
			else:
				health -= damage
			
			@warning_ignore("shadowed_variable")
			var magic = MagicManager.calculate_damage()
			if magic > 0.0:
				show_magic(magic)
				health -= magic
			
			if health <= 0:
				$enemy_health_bar.visible = false
				$area.visible = false
				
				var first_number = EnemyManager.get_health() / 2
				var second_number = round(first_number / 1.2)
				var points = randf_range(second_number, first_number)
				$game_over_panel/points.text = "%.1f" % points
				PointsManager.earn_points(points)
				
				EnemyManager.add_health()
				EnemyManager.add_level()
				
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
		$game_over_panel.visible = true

func _on_timer_timeout() -> void:
	hit = true

func _on_crit_timer_timeout() -> void:
	crit_label.visible = false

func _on_magic_timer_timeout() -> void:
	magic_label.visible = false
