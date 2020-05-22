#!/usr/bin/python3
import pygame
import socket
import sys
import cv2
import numpy as np
from threading import Thread


class ClientSocketCar(object):
    '''
    实例客户端套接字,用于发送数据
    '''

    def __init__(self):
        '''
        初始化套接字
        '''
        self.clinet_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建套接字
        self.clinet_socket.connect(('172.17.131.49', 8888))  # ip地址 ,端口号192.168.199.230

    # 发送数据
    def run_socket(self):
        self.clinet_socket.send('$1,0,0,0,0,0,0,0,0,0#\n'.encode('utf-8'))

    def back_socket(self):
        self.clinet_socket.send('$2,0,0,0,0,0,0,0,0,0#\n'.encode('utf-8'))

    def runleft_socket(self):
        self.clinet_socket.send('$3,0,0,0,0,0,0,0,0,0#\n'.encode('utf-8'))

    def runright_socket(self):
        self.clinet_socket.send('$4,0,0,0,0,0,0,0,0,0#\n'.encode('utf-8'))

    def up_socket(self):
        self.clinet_socket.send('$0,0,0,0,3,0,0,0,0,0#\n'.encode('utf-8'))

    def down_socket(self):
        self.clinet_socket.send('$0,0,0,0,4,0,0,0,0,0#\n'.encode('utf-8'))

    def left_socket(self):
        self.clinet_socket.send('$0,0,0,0,6,0,0,0,0,0#\n'.encode('utf-8'))

    def right_socket(self):
        self.clinet_socket.send('$0,0,0,0,7,0,0,0,0,0#\n'.encode('utf-8'))

    def yuanleft_socket(self):
        self.clinet_socket.send('$0,1,0,0,0,0,0,0,0,0#\n'.encode('utf-8'))

    def yuanright_socket(self):
        self.clinet_socket.send('$0,2,0,0,0,0,0,0,0,0#\n'.encode('utf-8'))

    def di_socket(self):
        self.clinet_socket.send('$0,0,1,0,0,0,0,0,0,0#\n'.encode('utf-8'))

    def jiasu_socket(self):
        self.clinet_socket.send('$0,0,0,1,0,0,0,0,0,0#\n'.encode('utf-8'))

    def jiansu_socket(self):
        self.clinet_socket.send('$0,0,0,2,0,0,0,0,0,0#\n'.encode('utf-8'))

    def huo_socket(self):
        self.clinet_socket.send('$0,0,0,0,0,0,0,1,0,0#\n'.encode('utf-8'))

    def stop_socket(self):
        self.clinet_socket.send('$0,0,0,0,8,0,0,0,0,0#\n'.encode('utf-8'))

    def recv_socket(self):
        return self.clinet_socket.recv(1024)

    def __del__(self):
        self.clinet_socket.close()


class Point(object):
    '''
    创建按钮类
    '''

    # 初始化
    def __init__(self):
        # # 实例化socket对象
        self.car_socket = ClientSocketCar()
        # # 载入图片
        # self.image_point1 = pygame.image.load('point_vert.png')  # 图片1
        # self.image_point2 = pygame.image.load('point_horiz.png')  # 图片2
        # # 将图片对象转化成矩形对象
        # self.img_rect1 = self.image_point1.get_rect()  # 矩形1 centerx=100, centery=130
        # self.img_rect2 = self.image_point2.get_rect()  # 矩形2 centerx=390, centery=130
        # self.img_rect1.move_ip(100, 130)
        # self.img_rect2.move_ip(390, 130)
        # # 按钮步进速度
        # self.speed = 8

    def move_runleft(self):
        '''
        按钮向左移动,并通过socket向服务端发送数据
        '''
        # 判断矩形对象的x方向位置
        # if self.img_rect2[0] > 295:
        # self.img_rect2.move_ip(-self.speed, 0)
        self.car_socket.runleft_socket()

    def move_runright(self):
        '''
        按钮向右移动,并通过socket向服务端发送数据
        '''
        # 判断矩形对象的x方向位置
        # if self.img_rect2[0] < 485:
        # 改变按钮位置
        # self.img_rect2.move_ip(self.speed, 0)
        # 发送数据
        self.car_socket.runright_socket()

    def move_run(self):
        '''
        按钮向上移动,并通过socket向服务端发送数据
        '''
        # 判断矩形对象的y方向位置
        # if self.img_rect1[1] > 44:
        # self.img_rect1.move_ip(0, -self.speed)
        self.car_socket.run_socket()

    def move_back(self):
        '''
        按钮向下移动,并通过socket向服务端发送数据
        '''
        # 判断矩形对象的y方向位置
        # if self.img_rect1[1] < 235:
        # self.img_rect1.move_ip(0, self.speed)
        self.car_socket.back_socket()

    def move_left(self):
        '''
        按钮向左移动,并通过socket向服务端发送数据
        '''
        # 判断矩形对象的x方向位置
        self.car_socket.left_socket()

    def move_right(self):
        '''
        按钮向右移动,并通过socket向服务端发送数据
        '''
        # 判断矩形对象的x方向位置
        self.car_socket.right_socket()

    def move_yuanleft(self):
        '''
        按钮向左移动,并通过socket向服务端发送数据
        '''
        # 判断矩形对象的x方向位置
        self.car_socket.yuanleft_socket()

    def move_yuanright(self):
        '''
        按钮向右移动,并通过socket向服务端发送数据
        '''
        # 判断矩形对象的x方向位置
        self.car_socket.yuanright_socket()

    def move_di(self):
        '''
        按钮向右移动,并通过socket向服务端发送数据
        '''
        # 判断矩形对象的x方向位置
        self.car_socket.di_socket()

    def move_jiasu(self):
        '''
        按钮向右移动,并通过socket向服务端发送数据
        '''
        # 判断矩形对象的x方向位置
        self.car_socket.jiasu_socket()

    def move_jiansu(self):
        '''
        按钮向右移动,并通过socket向服务端发送数据
        '''
        # 判断矩形对象的x方向位置
        self.car_socket.jiansu_socket()

    def move_huo(self):
        '''
        按钮向右移动,并通过socket向服务端发送数据
        '''
        # 判断矩形对象的x方向位置
        self.car_socket.huo_socket()

    def move_up(self):
        '''
        按钮向上移动,并通过socket向服务端发送数据
        '''
        # 判断矩形对象的y方向位置
        self.car_socket.up_socket()

    def move_down(self):
        '''
        按钮向下移动,并通过socket向服务端发送数据
        '''
        # 判断矩形对象的y方向位置
        self.car_socket.down_socket()

    def move_stop(self):
        '''
        按钮向下移动,并通过socket向服务端发送数据
        '''
        # 判断矩形对象的y方向位置
        # if self.img_rect1[1] < 235:
        # self.img_rect1.move_ip(0, self.speed)
        self.car_socket.stop_socket()

    def move_recv(self):
        return self.car_socket.recv_socket()

    def move_del(self):
        self.car_socket.__del__()


class Windows(object):
    '''
    创建主窗口类
    '''

    # 初始化
    def __init__(self):
        # pygame 硬件初始化
        pygame.init()
        self.window = pygame.display.set_mode([640, 480])
        # 初始化界面及背景
        pygame.display.set_caption('小车控制')
        # self.image = pygame.image.load('car.png')
        # 实例化按钮
        self.point_img = Point()

    def draw(self):
        '''
        将背景及按钮放入到主窗口
        '''
        # self.window.blit(self.image, (0, 0))
        # self.window.blit(self.point_img.image_point1, (self.point_img.img_rect1[0], self.point_img.img_rect1[1]))
        # self.window.blit(self.point_img.image_point2, (self.point_img.img_rect2[0], self.point_img.img_rect2[1]))
        try:
            path = "http://172.17.131.49:8080/?action=stream"
            cap = cv2.VideoCapture(path)
            FPS = 60
            pygame.time.Clock().tick(FPS)
            ret, frame = cap.read()
            cv2.putText(frame, he.decode("gbk"), (20, 25), cv2.FONT_HERSHEY_PLAIN, 1.3, (0, 255, 0), 2)
            if ret == True:  # 判断视频是否播放完毕
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = np.rot90(frame, k=-1)
                frame = pygame.surfarray.make_surface(frame)
                frame = pygame.transform.flip(frame, False, True)
            self.window.blit(frame, (0, 0))
        except:
            pass

    def event(self):
        '''
        检测并对事件进行响应
        '''
        # 获取当前事件类型,进行遍历
        self.event_list = pygame.event.get()
        for event in self.event_list:
            if event.type == pygame.QUIT:
                self.point_img.move_del()
                self.game_over()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.point_img.move_run()
                    print('加速加速--')
                if event.key == pygame.K_s:
                    self.point_img.move_back()
                    print('减速减速--')
                if event.key == pygame.K_a:
                    self.point_img.move_runleft()
                    print('左拐左拐--')
                if event.key == pygame.K_d:
                    self.point_img.move_runright()
                    print('右拐右拐--')
                if event.key == pygame.K_UP:
                    self.point_img.move_up()
                    print('摄上')
                if event.key == pygame.K_DOWN:
                    self.point_img.move_down()
                    print('摄下')
                if event.key == pygame.K_LEFT:
                    self.point_img.move_left()
                    print('摄左')
                if event.key == pygame.K_RIGHT:
                    self.point_img.move_right()
                    print('摄右')
                if event.key == pygame.K_n:
                    self.point_img.move_yuanleft()
                    print('原地左')
                if event.key == pygame.K_m:
                    self.point_img.move_yuanright()
                    print('原地右')
                if event.key == pygame.K_SPACE:
                    self.point_img.move_di()
                    print('鸣笛')
                if event.key == pygame.K_PERIOD:
                    self.point_img.move_jiasu()
                    print('加速')
                if event.key == pygame.K_COMMA:
                    self.point_img.move_jiansu()
                    print('减速')
                if event.key == pygame.K_j:
                    self.point_img.move_huo()
                    print('灭火')

            if event.type == pygame.KEYUP:
                self.point_img.move_stop()
                print('停止')

    def update(self):
        '''
        更新画面信息显示
        '''
        pygame.display.update()

    def xianshi(self):
        global he
        he = ''
        while True:
            he = self.point_img.move_recv()
            print(he.decode("gbk"))

    def game_over(self):
        '''
        系统退出
        '''
        pygame.quit()
        sys.exit()

    def run(self):
        '''
        程序运行入口
        '''
        thread = Thread(target=self.xianshi)
        thread.start()

        while True:
            self.draw()
            self.event()
            self.update()


if __name__ == '__main__':
    kong = Windows()
    kong.run()
