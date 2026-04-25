import math
import random
import tkinter as tk


WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
ARENA_MARGIN = 40
PLAYER_RADIUS = 18
PROJECTILE_RADIUS = 6
MOVE_SPEED = 5
PROJECTILE_SPEED = 10
WINNING_SCORE = 5
ROUND_DELAY_MS = 1500


class Player:
    def __init__(self, name, color, start_x, start_y, controls):
        self.name = name
        self.color = color
        self.start_x = start_x
        self.start_y = start_y
        self.controls = controls
        self.reset()

    def reset(self):
        self.x = self.start_x
        self.y = self.start_y
        self.direction = 0
        self.cooldown = 0

    def move(self, dx, dy):
        if dx == 0 and dy == 0:
            return

        length = math.hypot(dx, dy)
        dx = dx / length
        dy = dy / length
        self.x += dx * MOVE_SPEED
        self.y += dy * MOVE_SPEED
        self.direction = math.atan2(dy, dx)

        self.x = max(ARENA_MARGIN + PLAYER_RADIUS, min(WINDOW_WIDTH - ARENA_MARGIN - PLAYER_RADIUS, self.x))
        self.y = max(ARENA_MARGIN + PLAYER_RADIUS, min(WINDOW_HEIGHT - ARENA_MARGIN - PLAYER_RADIUS, self.y))


class Projectile:
    def __init__(self, x, y, dx, dy, color, owner):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color
        self.owner = owner

    def update(self):
        self.x += self.dx * PROJECTILE_SPEED
        self.y += self.dy * PROJECTILE_SPEED

    def out_of_bounds(self):
        return (
            self.x < ARENA_MARGIN
            or self.x > WINDOW_WIDTH - ARENA_MARGIN
            or self.y < ARENA_MARGIN
            or self.y > WINDOW_HEIGHT - ARENA_MARGIN
        )


class BattleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Offline Two Player Battle")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="#101820", highlightthickness=0)
        self.canvas.pack()

        self.keys_pressed = set()
        self.projectiles = []
        self.round_over = False
        self.message = "First team to 5 points wins"
        self.scores = {"Blue": 0, "Red": 0}

        self.players = [
            Player(
                "Blue Team",
                "#5dade2",
                ARENA_MARGIN + 100,
                WINDOW_HEIGHT // 2,
                {
                    "up": "w",
                    "down": "s",
                    "left": "a",
                    "right": "d",
                    "shoot": "space",
                },
            ),
            Player(
                "Red Team",
                "#ec7063",
                WINDOW_WIDTH - ARENA_MARGIN - 100,
                WINDOW_HEIGHT // 2,
                {
                    "up": "Up",
                    "down": "Down",
                    "left": "Left",
                    "right": "Right",
                    "shoot": "Return",
                },
            ),
        ]

        self.root.bind("<KeyPress>", self.on_key_press)
        self.root.bind("<KeyRelease>", self.on_key_release)

        self.draw()
        self.game_loop()

    def on_key_press(self, event):
        self.keys_pressed.add(event.keysym)

    def on_key_release(self, event):
        self.keys_pressed.discard(event.keysym)

    def game_loop(self):
        if not self.round_over:
            self.update_players()
            self.update_projectiles()
        self.draw()
        self.root.after(16, self.game_loop)

    def update_players(self):
        for player in self.players:
            dx = 0
            dy = 0
            if player.controls["up"] in self.keys_pressed:
                dy -= 1
            if player.controls["down"] in self.keys_pressed:
                dy += 1
            if player.controls["left"] in self.keys_pressed:
                dx -= 1
            if player.controls["right"] in self.keys_pressed:
                dx += 1

            player.move(dx, dy)

            if player.cooldown > 0:
                player.cooldown -= 1

            if player.controls["shoot"] in self.keys_pressed and player.cooldown == 0:
                self.fire_projectile(player)
                player.cooldown = 20

    def fire_projectile(self, player):
        dx = math.cos(player.direction)
        dy = math.sin(player.direction)
        if abs(dx) < 0.01 and abs(dy) < 0.01:
            dx = 1 if player.name == "Blue Team" else -1
            dy = 0

        start_x = player.x + dx * (PLAYER_RADIUS + PROJECTILE_RADIUS)
        start_y = player.y + dy * (PLAYER_RADIUS + PROJECTILE_RADIUS)
        self.projectiles.append(Projectile(start_x, start_y, dx, dy, player.color, player.name))

    def update_projectiles(self):
        active_projectiles = []
        for projectile in self.projectiles:
            projectile.update()
            if projectile.out_of_bounds():
                continue

            hit_player = self.check_hit(projectile)
            if hit_player:
                self.handle_score(projectile.owner, hit_player.name)
                return

            active_projectiles.append(projectile)

        self.projectiles = active_projectiles

    def check_hit(self, projectile):
        for player in self.players:
            if player.name == projectile.owner:
                continue
            distance = math.hypot(projectile.x - player.x, projectile.y - player.y)
            if distance <= PLAYER_RADIUS + PROJECTILE_RADIUS:
                return player
        return None

    def handle_score(self, scorer_name, target_name):
        self.round_over = True
        scoring_team = "Blue" if scorer_name == "Blue Team" else "Red"
        self.scores[scoring_team] += 1

        if self.scores[scoring_team] >= WINNING_SCORE:
            self.message = f"{scorer_name} wins the match! Press R to restart."
        else:
            self.message = f"{scorer_name} scored against {target_name}!"
            self.root.after(ROUND_DELAY_MS, self.reset_round)

    def reset_round(self):
        self.projectiles.clear()
        self.round_over = False
        self.message = "Battle on!"
        for player in self.players:
            player.reset()
        self.randomize_spawn_offset()

    def randomize_spawn_offset(self):
        offset = random.randint(-120, 120)
        self.players[0].start_y = WINDOW_HEIGHT // 2 + offset
        self.players[1].start_y = WINDOW_HEIGHT // 2 - offset
        for player in self.players:
            player.reset()

    def restart_match(self):
        self.scores = {"Blue": 0, "Red": 0}
        self.message = "First team to 5 points wins"
        self.projectiles.clear()
        self.round_over = False
        self.players[0].start_x = ARENA_MARGIN + 100
        self.players[1].start_x = WINDOW_WIDTH - ARENA_MARGIN - 100
        self.players[0].start_y = WINDOW_HEIGHT // 2
        self.players[1].start_y = WINDOW_HEIGHT // 2
        for player in self.players:
            player.reset()

    def draw(self):
        self.canvas.delete("all")
        self.draw_arena()
        self.draw_scoreboard()
        self.draw_controls()
        self.draw_players()
        self.draw_projectiles()
        self.draw_message()

        if "r" in self.keys_pressed and self.round_over and ("wins the match" in self.message):
            self.restart_match()

    def draw_arena(self):
        self.canvas.create_rectangle(
            ARENA_MARGIN,
            ARENA_MARGIN,
            WINDOW_WIDTH - ARENA_MARGIN,
            WINDOW_HEIGHT - ARENA_MARGIN,
            outline="#f7dc6f",
            width=3,
        )
        self.canvas.create_line(
            WINDOW_WIDTH // 2,
            ARENA_MARGIN,
            WINDOW_WIDTH // 2,
            WINDOW_HEIGHT - ARENA_MARGIN,
            fill="#566573",
            dash=(10, 8),
            width=2,
        )

    def draw_scoreboard(self):
        self.canvas.create_text(
            170,
            28,
            text=f"Blue Team: {self.scores['Blue']}",
            fill="#d6eaf8",
            font=("Helvetica", 18, "bold"),
        )
        self.canvas.create_text(
            WINDOW_WIDTH - 170,
            28,
            text=f"Red Team: {self.scores['Red']}",
            fill="#fadbd8",
            font=("Helvetica", 18, "bold"),
        )

    def draw_controls(self):
        self.canvas.create_text(
            200,
            WINDOW_HEIGHT - 18,
            text="Blue: W A S D to move, Space to shoot",
            fill="#d5dbdb",
            font=("Helvetica", 12),
        )
        self.canvas.create_text(
            WINDOW_WIDTH - 220,
            WINDOW_HEIGHT - 18,
            text="Red: Arrow keys to move, Enter to shoot",
            fill="#d5dbdb",
            font=("Helvetica", 12),
        )

    def draw_players(self):
        for player in self.players:
            self.canvas.create_oval(
                player.x - PLAYER_RADIUS,
                player.y - PLAYER_RADIUS,
                player.x + PLAYER_RADIUS,
                player.y + PLAYER_RADIUS,
                fill=player.color,
                outline="white",
                width=2,
            )
            aim_x = player.x + math.cos(player.direction) * 28
            aim_y = player.y + math.sin(player.direction) * 28
            self.canvas.create_line(player.x, player.y, aim_x, aim_y, fill="white", width=3)

    def draw_projectiles(self):
        for projectile in self.projectiles:
            self.canvas.create_oval(
                projectile.x - PROJECTILE_RADIUS,
                projectile.y - PROJECTILE_RADIUS,
                projectile.x + PROJECTILE_RADIUS,
                projectile.y + PROJECTILE_RADIUS,
                fill=projectile.color,
                outline="white",
            )

    def draw_message(self):
        self.canvas.create_text(
            WINDOW_WIDTH // 2,
            28,
            text=self.message,
            fill="#f8f9f9",
            font=("Helvetica", 16, "bold"),
        )


def main():
    root = tk.Tk()
    game = BattleGame(root)

    def restart_key(event):
        if event.keysym.lower() == "r":
            game.restart_match()

    root.bind("<KeyPress-r>", restart_key)
    root.bind("<KeyPress-R>", restart_key)
    root.mainloop()


if __name__ == "__main__":
    main()
