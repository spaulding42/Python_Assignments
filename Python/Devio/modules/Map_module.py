import pygame
from config.mysqlconnection import connectToMySQL

from settings import *
import math
import random


# from modules import object
DATABASE = 'devio_level_schema'
BRICK = pygame.transform.scale(pygame.image.load('assets/brick.png'), (50,50))

def collide(obj1,obj2,offset):
    offset_x = obj2.x - (obj1.x + offset)
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x,offset_y)) != None

# if the class is a basic Object it cannot move
class Object:
    def __init__(self,data):
        self.id = data['id']
        self.x = data['x_value']
        self.y = data['y_value']
        self.img = data['img']
        self.mask = pygame.mask.from_surface(self.img)
        self.type = data['type']
        
    def draw(self, window,x_offset):
        window.blit(self.img, (self.x + x_offset,self.y))

#  Entity class covers the things that can move and hurt the player
class Entity(Object):
    def __init__(self,data):
        super().__init__(data)
        self.grounded = True
        self.jump_power = 0
        self.jump_velocity = 0
        self.falling = 0
        self.velocity = 0
        self.direction = "right"
        self.status = "stationary"
        self.starting_x = self.x
        self.starting_y = self.y
        self.next_jump = 0

    def jump(self, bricks, x_offset,countdown,score): #----------------------------------------------------JUMP
        if self.status == "jumping":
            if self.jump_velocity > 0 and self.y + self.img.get_height() <= FLOOR:
                self.y = self.y - math.floor((self.jump_velocity/10))
                self.jump_velocity -=2
            for brick in bricks:
                    if collide(brick,self,x_offset):
                        self.y = self.y + math.floor((self.jump_velocity/10)) +10
                        self.jump_velocity = 0
                        if brick.type == 'brick' and self.type == "player":
                            bricks.remove(brick)
                            score += 25
                            BREAK_BRICK_SOUND.play()
                        if brick.type == "spikeybrick":
                            countdown = 0
                            DEATH_SOUND.play()
        return bricks, countdown, score

    def gravity(self, bricks, enemies, x_offset,countdown, score): #--------------------------------------------gravity
        # if self.type != 'spikeyblock':
        if self.y + self.img.get_height() >= FLOOR:
            self.y = FLOOR - self.img.get_height()
            self.grounded = True
            self.falling = 0
        else:
            
            self.y = self.y + (2 + math.floor(self.falling/10))
            self.falling += 1
            if self.type == 'player':
                for brick in bricks:
                    if collide(brick,self,x_offset):
                        if brick.type == "spikeybrick":
                            countdown = 0
                            DEATH_SOUND.play()
                        else:
                            self.y = self.y - (2 + math.floor(self.falling/10))
                            self.grounded = True
                            self.falling = 0
                for enemy in enemies:
                    if collide(enemy,self,x_offset):
                        self.jump_velocity += 100
                        self.falling = 0
                        enemies.remove(enemy)
                        score += 50
                        HIT_ENEMY_SOUND.play()
            if self.type == 'turtle' or self.type == "angrybrick" or self.type == "jumperguy":
                for brick in bricks:
                    if collide(brick,self,0):
                        self.y = self.y - (2 + math.floor(self.falling/10))
                        self.grounded = True
                        self.falling = 0
            
        return enemies, countdown, score

    def move(self, bricks):
        if self.direction == "left":
            self.x -= self.velocity
            for brick in bricks:
                if collide(brick,self,0):
                    self.direction = "right"
                    self.x += self.velocity
                    self.img = pygame.transform.flip(self.img, True, False)

        if self.direction == "right":
            self.x += self.velocity
            for brick in bricks:
                if collide(brick,self,0):
                    self.direction = "left"
                    self.x -= self.velocity
                    self.img = pygame.transform.flip(self.img, True, False)
                    
    def animate(self,timer):
        if self.type == 'player':
            if timer%30 == 0: #Stationary Animations
                if self.direction == 'left':
                    if self.status == "stationary":
                        if self.img == DEVIO_LEFT_STANDING_1:
                            self.img = DEVIO_LEFT_STANDING_2
                        else:
                            self.img = DEVIO_LEFT_STANDING_1
                if self.direction == 'right':
                    if self.status == "stationary":
                        if self.img == DEVIO_RIGHT_STANDING_1:
                            self.img = DEVIO_RIGHT_STANDING_2
                        else:
                            self.img = DEVIO_RIGHT_STANDING_1
            if timer == 0 or timer == 30: # WALKING Animations
                # print(f"{self.status} plus {self.direction} at {timer}")
                if self.status == 'walking' and self.direction == "right":
                    self.img = DEVIO_RIGHT_STANDING_1
                if self.status == 'walking' and self.direction == "left":
                    self.img = DEVIO_LEFT_STANDING_1
            if timer == 10 or timer == 40: # WALKING Animations
                if self.status == 'walking' and self.direction == "right":
                    self.img = DEVIO_RIGHT_WALKING_1
                if self.status == 'walking' and self.direction == "left":
                    self.img = DEVIO_LEFT_WALKING_1
            if timer == 20 or timer == 50: # WALKING Animations
                if self.status == 'walking' and self.direction == "right":
                    self.img = DEVIO_RIGHT_WALKING_2
                if self.status == 'walking' and self.direction == "left":
                    self.img = DEVIO_LEFT_WALKING_2
            if  self.status == 'jumping':
                if self.direction == 'right':
                    self.img = DEVIO_RIGHT_JUMPING
                else:
                    self.img = DEVIO_LEFT_JUMPING
            if self.status == 'stationary' and self.img == DEVIO_LEFT_JUMPING:
                self.img = DEVIO_LEFT_STANDING_1
            if self.status == 'stationary' and self.img == DEVIO_RIGHT_JUMPING:
                self.img = DEVIO_RIGHT_STANDING_1


# ----------- MAP CLASS-----------------------------------------------------MAP CLASS----------
class Map:
    def __init__(self,data):
        self.name = data['name']
        self.id = data['id']
        self.type = data['type']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.map_items = []
        self.map_entities = []
        self.deleted_indexes = []
    
    @classmethod
    def load_map_by_name(cls,data):
        query = "SELECT * FROM levels JOIN terrain_objects ON levels.id = terrain_objects.level_id WHERE levels.name = %(name)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        
        if results:
            map = cls(results[0])
            for item in results:
                
                item_data = {
                    'id': item['terrain_objects.id'],
                    'type': item['terrain_objects.type'],
                    'x_value': item['x_value'],
                    'y_value': item['y_value'],
                    'img': item['img'],
                }
                # print(item_data)
                if item['terrain_objects.type'] == 'brick':
                    item_data['img'] = BRICK
                    item_instance = Object(item_data)
                    map.map_items.append(item_instance)
                if item['terrain_objects.type'] == 'stone':
                    item_data['img'] = STONE
                    item_instance = Object(item_data)
                    map.map_items.append(item_instance)
                if item['terrain_objects.type'] == 'spikeybrick':
                    item_data['img'] = SPIKEY_BRICK
                    item_instance = Object(item_data)
                    map.map_items.append(item_instance)

                if item['terrain_objects.type'] == 'turtle':
                    item_data['img'] = TURTLE
                    entity_instance = Entity(item_data)
                    entity_instance.direction = "left"
                    entity_instance.velocity = 2
                    map.map_entities.append(entity_instance)
                if item['terrain_objects.type'] == 'angrybrick':
                    item_data['img'] = ANGRY_BRICK
                    entity_instance = Entity(item_data)
                    entity_instance.jump_power = 110
                    entity_instance.next_jump = random.randrange(2,6) * 60
                    map.map_entities.append(entity_instance)
                if item['terrain_objects.type'] == 'jumperguy':
                    item_data['img'] = JUMPER_GUY
                    entity_instance = Entity(item_data)
                    entity_instance.velocity = 2
                    entity_instance.jump_power = 110
                    entity_instance.next_jump = random.randrange(2,6) * 60
                    map.map_entities.append(entity_instance)
                
                if item['terrain_objects.type'] == 'end_door':
                    item_data['img'] = END_DOOR
                    item_instance = Object(item_data)
                    map.map_items.append(item_instance)
        
            return map
        

    def save_map(self):
        # delete items that were deleted from map and came from DB upon loading
        for item in self.deleted_indexes:
            query = f"DELETE FROM terrain_objects WHERE id = '{item.id}'"
            connectToMySQL(DATABASE).query_db(query)

        for map_item in self.map_items:
            if map_item.id == -2:
                item_info = {
                    'type': map_item.type,
                    'x_value': map_item.x,
                    'y_value': map_item.y,
                    'img': map_item.img,
                    'level_id': self.id
                }
                query = "INSERT INTO terrain_objects (type, x_value,y_value,img,level_id) VALUES (%(type)s, %(x_value)s, %(y_value)s, %(img)s, %(level_id)s);"
                connectToMySQL(DATABASE).query_db(query, item_info)
        for map_entity in self.map_entities:
            if map_entity.type != 'player' and map_entity.id == -2:
                print(map_entity.type)
                entity_info = {
                    'type': map_entity.type,
                    'x_value': map_entity.starting_x,
                    'y_value': map_entity.starting_y,
                    'img': map_entity.img,
                    'level_id': self.id
                }
                query = "INSERT INTO terrain_objects (type, x_value,y_value,img,level_id) VALUES (%(type)s, %(x_value)s, %(y_value)s, %(img)s, %(level_id)s);"
                connectToMySQL(DATABASE).query_db(query, entity_info)
    
    @classmethod
    def list_all_maps(cls):
        query = "SELECT * FROM levels;"
        results = connectToMySQL(DATABASE).query_db(query)
        level_list = []
        if results:
            for level in results:
                level_instance = cls(level)
                level_list.append(level_instance)
        return level_list