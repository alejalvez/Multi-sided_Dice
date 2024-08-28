#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import math
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from shape_dictionary import *

def loadTexture(shape_choice):
    #The number 0 should choose the texture the tetrahedron, 1 the cube, 2 the octahedron, 3 the dodecahedron, and 4 the icosahedron. 
    options = ('tetrahedron','cube','octahedron','dodecahedron','icosahedron')
    file_name = str(options[shape_choice]) + '_sides.png'
    textureSurface = pygame.image.load(file_name)
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid

def Tetrahedron():
    tetra = shape_data['Tetrahedron']
    vertices = tetra['vertices']
    edges = tetra['edges']
    texture_coords = tetra['texture_coords']
    surfaces = tetra['surfaces']
    normals = tetra['normals']
    vertex_colors = [
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1)
    ]

    loadTexture(0)

    glBegin(GL_TRIANGLES)
    for surface_index,surface in enumerate(surfaces):
        glNormal3fv(normals[surface_index])
        for vertex_index,vertex in enumerate(surface):
            glColor3fv(vertex_colors[vertex%3])
            glTexCoord2fv(texture_coords[surface_index][vertex_index])
            glVertex3fv(vertices[vertex])
    glEnd()
    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((1,1,1))
            glVertex3fv(vertices[vertex])
    glEnd()
  

def Cube():

    cube = shape_data['Cube']
    vertices = cube['vertices']
    edges = cube['edges']
    texture_coords = cube['texture_coords']
    surfaces = cube['surfaces']
    normals = cube['normals']
    vertex_colors = [
        (1, 0, 0),
        (0, 0, 1)
    ]


    loadTexture(1)

    glBegin(GL_QUADS)
    for surface_index,surface in enumerate(surfaces):
        glNormal3fv(normals[surface_index])
        for vertex_index,vertex in enumerate(surface):
            glColor3fv(vertex_colors[vertex%2])
            glTexCoord2fv(texture_coords[surface_index][vertex_index])
            glVertex3fv(vertices[vertex])
    glEnd()
    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((1,1,1))
            glVertex3fv(vertices[vertex])
    glEnd()
    #Draw(vertices, edges)


def Octahedron():
    oct = shape_data['Octahedron']
    vertices = oct['vertices']
    edges = oct['edges']
    texture_coords = oct['texture_coords']
    surfaces = oct['surfaces']
    normals = oct['normals']
    vertex_colors = [
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1)
    ]


    loadTexture(2)

    glBegin(GL_TRIANGLES)
    for surface_index,surface in enumerate(surfaces):
        glNormal3fv(normals[surface_index])
        for vertex_index,vertex in enumerate(surface):
            glColor3fv(vertex_colors[vertex%3])
            glTexCoord2fv(texture_coords[surface_index][vertex_index])
            glVertex3fv(vertices[vertex])
    glEnd()
    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((1,1,1))
            glVertex3fv(vertices[vertex])
    glEnd()
    #Draw(vertices, edges)


def Dodecahedron():
    dod = shape_data['Dodecahedron']
    vertices = dod['vertices']
    edges = dod['edges']
    texture_coords = dod['texture_coords']
    surfaces = dod['surfaces']
    normals = dod['normals']
    vertex_colors = [
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
        (1,1,0),
        (1,0,1)
    ]

    loadTexture(3)

    for surface_index,surface in enumerate(surfaces):
        glNormal3fv(normals[surface_index])
        glBegin(GL_POLYGON)
        for vertex_index,vertex in enumerate(surface):
            glColor3fv(vertex_colors[vertex%5])
            glTexCoord2fv(texture_coords[surface_index][vertex_index])
            glVertex3fv(vertices[vertex])
        glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((1,1,1))
            glVertex3fv(vertices[vertex])
    glEnd()

    #Draw(vertices, edges)


def Icosahedron():
   
    icos = shape_data['Icosahedron']
    vertices = icos['vertices']
    edges = icos['edges']
    texture_coords = icos['texture_coords']
    surfaces = icos['surfaces']
    normals = icos['normals']
    vertex_colors = [
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1)
    ] 

    loadTexture(4)

    glBegin(GL_TRIANGLES)
    for surface_index,surface in enumerate(surfaces):
        glNormal3fv(normals[surface_index])
        for vertex_index,vertex in enumerate(surface):
            glColor3fv(vertex_colors[vertex%3])
            glTexCoord2fv(texture_coords[surface_index][vertex_index])
            glVertex3fv(vertices[vertex])
    glEnd()
    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((1,1,1))
            glVertex3fv(vertices[vertex])
    glEnd()



def main():
    pygame.init()
    display = (800,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glOrtho(-2, 2, -2, 2, -2, 2)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    
    shape = Cube
    
    glEnable(GL_LIGHT0)
    glLight(GL_LIGHT0, GL_POSITION,  (0, -5.0, 0, 1)) # point light from the below
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 0.2))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))

    glMaterialf(GL_FRONT, GL_SHININESS, 50.0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
                #quit()
        
        keys = pygame.key.get_pressed() # Get pressed keys
    
        # pick shape based on keys pressed
        options = {pygame.K_1:Tetrahedron, pygame.K_2:Cube, pygame.K_3:Octahedron,
                   pygame.K_4:Dodecahedron, pygame.K_5:Icosahedron}
        for key,value in options.items():
            if keys[key]:
                shape = value

        glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        shape()

        pygame.display.flip()
        pygame.time.wait(10)

main()