FlordeAbril.c
Quem pode acessar
Não compartilhado
Propriedades do sistema
Tipo
C
Tamanho
2 KB
Armazenamento usado
2 KB
Local
2014
Proprietário
eu
Modificado
13 de fev. de 2020 por mim
Aberto
16:23 por mim
Criado em
31 de mar. de 2015 com o Google Drive for desktop
Adicionar uma descrição
Os leitores podem fazer o download
//
//  main.m
//  Transformacoes1
//
//  Created by Marcelo Costa on 15/12/12.
//  Copyright (c) 2012 Universidade Federal de Alagoas - UFAL. All rights reserved.
//

//#import <Cocoa/Cocoa.h>
#import <GLUT/GLUT.h>   



void init (void)
{
    /* selecionar cor de fundo (preto) */
    glClearColor (0.0, 0.0, 0.0, 0.0);
    
    glMatrixMode (GL_PROJECTION); //Projecao 2D
    
    glOrtho(0.0, 500.0, 0.0, 400.0, -1.0, 1.0); //Definindo os limites da Porta de Visao (ViewPort)
    
}

void display(void)
{
    /* Limpar todos os pixels  */
    glClear (GL_COLOR_BUFFER_BIT);
    
    glColor3f (1.0, 1.0, .0);
    glBegin(GL_POLYGON);
        glVertex3f (249.0f, 250.0f, -1.0f);
        glVertex3f (251.0f, 250.0f, -1.0f);
        glVertex3f (249.0f, 100.0f, -1.0f);
        glVertex3f (251.0f, 100.0f, -1.0f);
    glEnd();
    
    /* Desenhar um polígono branco  */
    glColor3f (1.0, 1.0, 1.0);
    glBegin(GL_TRIANGLES);
        glVertex2f (250.0f, 250.0f);
        glVertex2f (230.0f, 200.0f);
        glVertex2f (270.0f, 200.0f);
    glEnd();
    
    /* Desenhar um polígono vermelho */
    glColor3f (1.0, 0.0, 0.0);
    glBegin(GL_TRIANGLES);
        glVertex2f (250.0f, 250.0f);
        glVertex2f (300.0f, 230.0f);
        glVertex2f (300.0f, 270.0f);
    glEnd();
    
    /* Desenhar um polígono verde */
    glColor3f (0.0, 1.0, 0.0);
    glBegin(GL_TRIANGLES);
        glVertex2f (250.0f, 250.0f);
        glVertex2f (230.0f, 300.0f);
        glVertex2f (270.0f, 300.0f);
    glEnd();
    
    /* Desenhar um polígono vermelho */
    glColor3f (0.0, 0.0, 1.0);
    glBegin(GL_TRIANGLES);
        glVertex2f (250.0f, 250.0f);
        glVertex2f (200.0f, 270.0f);
        glVertex2f (200.0f, 230.0f);
    glEnd();
    
    
    /* Não esperar! */
    glFlush ();
}



int main(int argc, char** argv) {
    
	glutInit(&argc, argv);
    
	glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize (500, 400);
	glutInitWindowPosition (200, 200);
	glutCreateWindow ("Flor de Abril");
    
	init ();
    
	glutDisplayFunc(display);
    
	glutMainLoop();
    
	/* C ANSI requer que main retorne um inteiro */
	return 0;
    
}
