#!/usr/bin/env python3
import sys
sys.path.append("prefabs/")
import os.path
import os
from PySide.QtCore import *
from PySide.QtGui import *
import importlib
import createPrefab
from PIL import Image
from PIL.ImageQt import ImageQt
import generateSkybox
import light_create
import subprocess
import pickle
import pprint
import random
import glob
import webbrowser
import wave
import zipfile
import shutil
import winsound

class GridBtn(QWidget):
    def __init__(self, parent, x, y, btn_id):
        super(GridBtn, self).__init__()
        self.button = QPushButton("", parent)
        self.x = x
        self.y = y
        self.btn_id = btn_id
        #self.button.move(self.x,self.y)
        self.button.resize(32,32)
        self.button.setFixedSize(32, 32)
        self.button.pressed.connect(lambda: self.click_func(parent, x, y,
                                                            btn_id))
        self.button.setMouseTracking(True)
        self.button.installEventFilter(self)
        self.button.show()
        self.icon = []
        for i in range(levels):
            self.icon.append(None)

    def reset_icon(self):
        self.button.setIcon(QIcon(""))

    def click_func(self, parent, x, y, btn_id, clicked=True, h_moduleName="None", h_icon=''): #h_moduleName and h_icon and h_rot are used when undoing/redoing
        global world_id_num
        global id_num
        global entity_num
        global entity_list
        global placeholder_list
        global icon
        global rotation
        global totalblocks
        global stored_info_list
        global stored_rotation_list
        global levels
        global rotation, currentfilename
        global history
        global redo_history

        current_list = eval('parent.tile_list%s' % str(parent.list_tab_widget.currentIndex()+1))

        #format | history.append((x,y,moduleName,self.icon,level))
        if clicked:
            redo_history=[]
            if self.icon[level]:
                moduleName = eval(prefab_list[parent.list_tab_widget.currentIndex()][current_list.currentRow()])
                templist=[(x,y,moduleName,self.icon[level],None)]
            else:
                templist=[(x,y,None,None,None)]

        def clear_btn(btn_id):
            self.button.setIcon(QIcon())
            totalblocks[level][btn_id] = ''
            entity_list[level][btn_id] = ''
            iconlist[level][btn_id] = ''
            stored_info_list[level][btn_id]=''
            self.icon[level] = None
        
        if self.checkForCtrl(clicked):
            clear_btn(btn_id)
        else:
            if clicked:
                moduleName = eval(prefab_list[parent.list_tab_widget.currentIndex()][current_list.currentRow()])
            else:
                moduleName = h_moduleName if h_moduleName != None else clear_btn(btn_id)

            if h_moduleName != None:
                if clicked:

                    try:
                        #gotta redo this. this is very inefficient and needs to be like the rest
                        #of the prefab lists
                        '''
                        current_prefab_icon_list = open('prefab_template/rot_prefab_list.txt', 'r+')
                        current_prefab_icon_list = current_prefab_icon_list.readlines()
                        current_prefab_icon_list = current_prefab_icon_list[parent.current_list.currentRow()]
                        if "\n" in current_prefab_icon_list:
                            current_prefab_icon_list = current_prefab_icon_list[:-1]
                        '''
               

                        current_prefab_icon_list = rotation_icon_list[parent.list_tab_widget.currentIndex()][current_list.currentRow()]
                        current_prefab_icon_list = open('prefab_template/iconlists/'+current_prefab_icon_list, 'r+')
                        current_prefab_icon_list = current_prefab_icon_list.readlines()
                        icon = current_prefab_icon_list[rotation]
                        if "\n" in icon:
                            icon = icon[:-1]
                    except Exception as e:
                        print(str(e))
                        icon = prefab_icon_list[parent.list_tab_widget.currentIndex()][current_list.currentRow()]
                        
                else:
                    icon = h_icon

                self.button.setIcon(QIcon(icon))
                self.button.setIconSize(QSize(32,32))
                iconlist[level][btn_id] = icon
                stored_info_list[level][btn_id] = [moduleName,x,y,id_num,world_id_num,entity_num,placeholder_list,rotation,level]

                self.icon[level] = icon
            else:
                stored_info_list[level][btn_id] = ""

            if "*" not in parent.windowTitle():
                parent.setWindowTitle("Easy TF2 Mapper* - ["+currentfilename+"]")
            
            if clicked:
                templist.append((x,y,moduleName,self.icon[level],None))
                history.append(templist)

    def checkForCtrl(self, clicked):
        if clicked:
            modifiers = QApplication.keyboardModifiers()
            if modifiers == Qt.ControlModifier:           
                return True
            else: 
                return False
        else:
            return False
        
class MainWindow(QMainWindow):
    def __init__(self):
        #create the main window
        super(MainWindow, self).__init__()
        self.setGeometry(100, 25, 875, 750)
        self.setWindowTitle("Easy TF2 Mapper")
        self.setWindowIcon(QIcon("icons\icon.ico"))
        namelist = ['gravelpit','2fort','upward','mvm']
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("icons/backgrounds/background_"+namelist[random.randint(0,3)]+".jpg")))
        self.setPalette(palette)

        #create menubar
        exitAction = QAction("&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit Application")
        exitAction.triggered.connect(self.close_application)

        openAction = QAction("&Open", self)
        openAction.setShortcut("Ctrl+O")
        openAction.setStatusTip("Open .vmf file")
        openAction.triggered.connect(self.file_open)

        saveAction = QAction("&Save", self)
        saveAction.setShortcut("Ctrl+S")
        saveAction.setStatusTip("Save File as .ezm save, allowing for use by others/you later.")
        saveAction.triggered.connect(self.file_save)
        
        saveAsAction = QAction("&Save As", self)
        saveAsAction.setShortcut("Ctrl+Shift+S")
        saveAsAction.setStatusTip("Save File as .ezm save, allowing for use by others/you later.")
        saveAsAction.triggered.connect(lambda: self.file_save(False, True))
        
        helpAction = QAction("&Wiki",self)
        helpAction.triggered.connect(lambda: webbrowser.open_new_tab('http://github.com/baldengineers/easytf2_mapper/wiki'))
        
        tutorialAction = QAction("&Reference Guide",self)
        tutorialAction.setStatusTip("Quick reference guide on the TF2Mapper website.")
        tutorialAction.triggered.connect(lambda: webbrowser.open_new_tab('http://tf2mapper.com/tutorial.html'))



        newAction = QAction("&New", self)
        newAction.setShortcut("Ctrl+n")
        newAction.setStatusTip("Create a New File")
        newAction.triggered.connect(lambda: self.grid_change(0,0,0,True,False,True))

        hammerAction = QAction("&Open Hammer",self)
        hammerAction.setShortcut("Ctrl+H")
        hammerAction.setStatusTip("Opens up Hammer.")
        hammerAction.triggered.connect(lambda: self.open_hammer(0,"null"))

        changeHammer = QAction("&Change Hammer Directory",self)
        changeHammer.setShortcut("Ctrl+Shift+H")
        changeHammer.setStatusTip("Changes default hammer directory.")
        changeHammer.triggered.connect(lambda: self.open_hammer(0,"null",True))

        changeLightAction = QAction("&Change Lighting", self)
        changeLightAction.setShortcut("Ctrl+J")
        changeLightAction.setStatusTip("Change the environment lighting of the map.")
        changeLightAction.triggered.connect(self.change_light)
        
        exportAction = QAction("&as .VMF", self)
        exportAction.setShortcut("Ctrl+E")
        exportAction.setStatusTip("Export as .vmf")
        exportAction.triggered.connect(self.file_export)

        undoAction = QAction("&Undo", self)
        undoAction.setShortcut("Ctrl+Z")
        undoAction.setStatusTip("Undo previous action")
        undoAction.triggered.connect(lambda: self.undo(True))

        redoAction = QAction("&Redo", self)
        redoAction.setShortcut("Ctrl+Shift+Z")
        redoAction.setStatusTip("Redo previous action")
        redoAction.triggered.connect(lambda: self.undo(False))
        
        removeAction = QAction("&Remove Last Prefab(s)",self)
        removeAction.setShortcut("Ctrl+R")
        removeAction.setStatusTip("Delete a variable amount of prefabs from the end of the list")
        removeAction.triggered.connect(self.remove_prefabs)

        gridAction = QAction("&Set Grid Size", self)
        gridAction.setShortcut("Ctrl+G")
        gridAction.setStatusTip("Set Grid Height and Width. RESETS ALL BLOCKS.")
        gridAction.triggered.connect(lambda: self.grid_change(0,0,0,True,False,True))

        createPrefabAction = QAction("&Create Prefab", self)
        createPrefabAction.setShortcut("Ctrl+I")
        createPrefabAction.setStatusTip("View the readme for a good idea on formatting Hammer Prefabs.")
        createPrefabAction.triggered.connect(self.create_prefab)

        consoleAction = QAction("&Open Dev Console", self)
        consoleAction.setShortcut("`")
        consoleAction.setStatusTip("Run functions/print variables manually")
        consoleAction.triggered.connect(self.open_console)

        changeSkybox = QAction("&Change Skybox", self)
        changeSkybox.setStatusTip("Change the skybox of the map.")
        changeSkybox.setShortcut("Ctrl+B")
        changeSkybox.triggered.connect(self.change_skybox)
        
        importPrefab = QAction("&Prefab",self)
        importPrefab.setStatusTip("Import a prefab in a .zip file. You can find some user-made ones at http://tf2mapper.com")
        importPrefab.setShortcut("Ctrl+Shift+I")
        importPrefab.triggered.connect(self.import_prefab)

        bspExportAction = QAction("&as .BSP",self)
        bspExportAction.setStatusTip("Export as .bsp")
        bspExportAction.setShortcut("Ctrl+Shift+E")
        bspExportAction.triggered.connect(self.file_export_bsp)
        
        self.statusBar()

        
        
        mainMenu = self.menuBar()
        
        
        fileMenu = mainMenu.addMenu("&File") 
        optionsMenu = mainMenu.addMenu("&Options")
        toolsMenu = mainMenu.addMenu("&Tools")
        helpMenu = mainMenu.addMenu("&Help")
        
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(saveAsAction)
        fileMenu.addSeparator()
        
        importMenu = fileMenu.addMenu("&Import")
        importMenu.addAction(importPrefab)

        exportMenu = fileMenu.addMenu("&Export")
        exportMenu.addAction(exportAction)
        exportMenu.addAction(bspExportAction)
        
        fileMenu.addSeparator()

        fileMenu.addAction(undoAction)
        fileMenu.addAction(redoAction)
        
        fileMenu.addSeparator()
        
        fileMenu.addAction(exitAction)

        optionsMenu.addAction(gridAction)
        optionsMenu.addAction(changeSkybox)
        optionsMenu.addAction(changeHammer)
        
        toolsMenu.addAction(createPrefabAction)
        toolsMenu.addAction(hammerAction)
        toolsMenu.addSeparator()
        toolsMenu.addAction(consoleAction)
        
        helpMenu.addAction(tutorialAction)
        helpMenu.addAction(helpAction)
        
        self.home()
        self.change_skybox()
        self.level_select()


        
    def open_hammer(self,loaded,file,reloc = False):
        self.open_file()
        if "loaded_first_time" not in self.files or reloc:
            self.file.close()
            self.open_file(True)
            hammer_location = QFileDialog.getOpenFileName(self, "Find Hammer Location", "/","Hammer Executable (*.exe *.bat)")
            hammer_location = str(hammer_location[0])
            self.file.write("loaded_first_time\n")
            self.file.write(hammer_location)
            self.file.close()
            if loaded == 1:
                subprocess.Popen(hammer_location +" "+ file)
            else:
                subprocess.Popen(hammer_location)
        else:
            
            try:
                if loaded == 1:
                    subprocess.Popen(self.fileloaded[1] + " "+file)
                else:
                    subprocess.Popen(self.fileloaded[1])
            except Exception as e:
                print(str(e))
                self.pootup = QMessageBox()
                self.pootup.setText("ERROR!")
                self.pootup.setInformativeText("Hammer executable/batch moved or renamed!")
                self.pootup.exec_()

                self.file.close()
                os.remove("startupcache/startup.su")
                self.open_hammer(0,"null")

    def open_file(self,reloc = False):
        if reloc:
            os.remove("startupcache/startup.su")
        
        try:
            self.file = open("startupcache/startup.su", "r+")
        except:
            self.file = open("startupcache/startup.su", "w+")
        self.fileloaded = self.file.readlines()
        self.files = "".join(self.fileloaded)

    def remove_prefabs(self):
        import removeText
        num = QInputDialog.getText(self,("Remove Prefabs"),("Remove x number of prefabs from the back of the list. REQUIRES RESTART"))
        try:
            num = int(num[0])
        except:
            QMessageBox.critical(self, "Error", "Please enter a number.")
            self.remove_prefabs()
        removeText.reset(num)

    def closeEvent(self, event):
        #closeEvent runs close_application when the x button is pressed
        event.ignore()
        self.close_application()
        
    def home(self):
        global levels, current_list
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.scrollArea = QScrollArea()

        self.scrollArea.setStyleSheet("background-color: rgb(50, 50, 50, 100);")

        self.scrollArea.setBackgroundRole(QPalette.Light)


    
        try:
            self.scrollArea.setGeometry(QRect(0, 0, self.grid_x*32, self.grid_y*32))
        except:
            self.scrollArea.setGeometry(QRect(0,0,580,580))
        try:
            if self.grid_x > 16:
                self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
            if self.grid_y > 16:
                self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        except:
            pass


        actiondict = {}
        self.buttonLabel = QLabel("Rotation:",self)
        self.levelLabel = QLabel("Level Select:",self)
        self.listLabel = QLabel("List of prefabs:",self)
        self.gridLabel = QLabel("Work Area:",self)
        
        self.divider = QFrame(self)
        self.divider.setFrameShape(QFrame.VLine)
        self.divider.setLineWidth(10)

        self.dividerH = QFrame(self)
        self.dividerH.setFrameShape(QFrame.HLine)
        self.dividerH.setLineWidth(10)

        self.current = QPushButton("",self)
        self.current.setIcon(QIcon(''))
        self.current.setIconSize(QSize(40,40))
        self.current.setFixedSize(QSize(40,40))
        self.current.setFlat(True)
        self.current.clicked.connect(self.heavy)

##'''
##        self.level = QPushButton(self)
##
##        self.level.setText("Level: 1")
##        
##        self.level.setFixedSize(QSize(150,30))
##        self.level.clicked.connect(self.level_select)
##'''

        self.levelSelect = QComboBox(self)
        self.levelSelect.currentIndexChanged.connect(lambda: self.change_level_new())

        self.levelup = QToolButton(self)
        self.levelup.setIcon(QIcon('icons/up.png'))
        self.levelup.setIconSize(QSize(20,20))
        self.levelup.clicked.connect(lambda: self.change_level(True, True))
        self.levelup.setAutoRaise(True)

        self.leveldown = QToolButton(self)
        self.leveldown.setIcon(QIcon('icons/down.png'))
        self.leveldown.setIconSize(QSize(20,20))
        self.leveldown.clicked.connect(lambda: self.change_level(True, False))
        self.leveldown.setAutoRaise(True)
        
        self.rotateCW = QToolButton(self)
        self.rotateCW.setShortcut(QKeySequence(Qt.Key_Right))
        self.rotateCW.setIcon(QIcon('icons/rotate_cw.png'))
        self.rotateCW.setIconSize(QSize(40,40))
        self.rotateCW.setFixedSize(QSize(40,40))
        self.rotateCW.setAutoRaise(True)

        self.rotateCCW = QToolButton(self)
        self.rotateCCW.setShortcut(QKeySequence(Qt.Key_Left))
        self.rotateCCW.setIcon(QIcon('icons/rotate_ccw.png'))
        self.rotateCCW.setIconSize(QSize(40,40))
        self.rotateCCW.setFixedSize(QSize(40,40))
        self.rotateCCW.setAutoRaise(True)

        #sets rotation value. 0 = right, 1 = down, 2 = left, 3 = right
        self.rotateCW.clicked.connect(self.rotateCW_func)
        self.rotateCCW.clicked.connect(self.rotateCCW_func)
        
        self.button_rotate_layout = QHBoxLayout()
        self.button_rotate_layout.addWidget(self.buttonLabel)
        self.button_rotate_layout.addWidget(self.rotateCCW)
        self.button_rotate_layout.addWidget(self.current)
        self.button_rotate_layout.addWidget(self.rotateCW)
        self.button_rotate_layout.addWidget(self.divider)
        self.button_rotate_layout.addWidget(self.levelLabel)
        self.button_rotate_layout.addWidget(self.levelSelect)
        self.button_rotate_layout.addWidget(self.levelup)
        self.button_rotate_layout.addWidget(self.leveldown)
        
        self.button_rotate_layout.addStretch(1)
            
        self.tile_list1 = QListWidget()
        #self.tile_list.setMaximumWidth(200)
        #self.tile_list.setStyleSheet("QListWidget { background-color: rgb(50, 50, 50, 100); }")
        self.tile_list2 = QListWidget()
        self.tile_list3 = QListWidget()
        
        self.list_tab_widget = QTabWidget()
        self.list_tab_widget.setMaximumWidth(200)
        self.list_tab_widget.addTab(self.tile_list1,'Geometry')
        self.list_tab_widget.addTab(self.tile_list2,'Map Layout')
        self.list_tab_widget.addTab(self.tile_list3,'Fun')
        self.list_tab_widget.currentChanged.connect(self.changeCurrentList)

        print("len:", self.list_tab_widget.count())
        #self.list_tab_widget.setStyleSheet("QTabWidget { background-color: rgb(50, 50, 50, 100); }")
        
        self.up_tool_btn = QToolButton(self)
        self.up_tool_btn.setIcon(QIcon('icons/up.png'))
        self.up_tool_btn.clicked.connect(self.prefab_list_up)
        
        self.down_tool_btn = QToolButton(self)
        self.down_tool_btn.setIcon(QIcon('icons/down.png'))
        self.down_tool_btn.clicked.connect(self.prefab_list_down)
        
        self.del_tool_btn = QToolButton(self)
        self.del_tool_btn.setIcon(QIcon('icons/delete.png'))
        self.del_tool_btn.clicked.connect(lambda: self.prefab_list_del(current_list.currentRow()))

        self.add_tool_btn = QToolButton(self)
        self.add_tool_btn.setIcon(QIcon('icons/add.png'))
        self.add_tool_btn.clicked.connect(self.create_prefab)
        
        self.tile_toolbar = QToolBar()
        self.tile_toolbar.addWidget(self.up_tool_btn)
        self.tile_toolbar.addSeparator()
        self.tile_toolbar.addWidget(self.down_tool_btn)
        self.tile_toolbar.addSeparator()
        self.tile_toolbar.addWidget(self.del_tool_btn)
        self.tile_toolbar.addSeparator()
        self.tile_toolbar.addWidget(self.add_tool_btn)


             
        for index, text in enumerate(prefab_text_list):
            for ind, indiv in enumerate(text):
                curr_list = eval("self.tile_list%d" % (index+1))
                item = QListWidgetItem(QIcon(prefab_icon_list[index][ind]), indiv)
                curr_list.addItem(item)
            
        for i in range(self.list_tab_widget.count()):
            eval("self.tile_list%d" %(i+1)).currentItemChanged.connect(self.changeIcon)

        #contains label and list vertically
        self.tile_list_layout = QVBoxLayout()
        self.tile_list_layout.addWidget(self.listLabel)
        self.tile_list_layout.addWidget(self.list_tab_widget)
        self.tile_list_layout.addWidget(self.tile_toolbar)
        
        self.button_grid_layout = QGridLayout()
        self.button_grid_layout.setSpacing(0)
        
        self.grid_widget = QWidget()
        self.grid_widget.setLayout(self.button_grid_layout)
        self.scrollArea.setWidget(self.grid_widget)
        self.scrollArea.setWidgetResizable(True)

        #contains label and grid vertically
        self.gridLayout = QVBoxLayout()
        self.gridLayout.addWidget(self.gridLabel)
        self.gridLayout.addWidget(self.scrollArea)
        self.button_grid_all = QVBoxLayout()
        self.button_grid_all.addLayout(self.button_rotate_layout)
        self.button_grid_all.addWidget(self.dividerH)
        self.button_grid_all.addLayout(self.gridLayout)
        
        self.column = QHBoxLayout()
        self.column.addLayout(self.button_grid_all)
        self.column.addLayout(self.tile_list_layout)
        
        self.row = QVBoxLayout(self.central_widget)
        self.row.addLayout(self.column)

        current_list = self.tile_list1
        
        try:
            f = open('startupcache/firsttime.su', 'r+')
            lines = f.readlines()
        except:
            f = open('startupcache/firsttime.su','w+')
            lines = f.readlines()
            
        if "startup" not in lines:
            '''
            self.popup = QMessageBox(self)
            self.popup.setGeometry(100,100,500,250)
            self.popup.setWindowTitle("First Launch")
            self.popup.setInformativeText("You haven't launched this before! Try looking at the <a href=\"https://github.com/baldengineers/easytf2_mapper/wiki/Texture-bug\">wiki</a> for help!")
            self.popup.setText("First Launch!")
            self.popup.exec_()
            #this is obsolete - jony
            '''

            QMessageBox.information(self, "First Launch", "First Launch!\n\nYou haven't launched this before! Try looking at the <a href=\"https://github.com/baldengineers/easytf2_mapper/wiki/Texture-bug\">wiki</a> for help!")
            f.write("startup")
            f.close
        
            #WILL ONLY WORK IN REDIST FORM
        else:
            pass
        
        self.grid_change(0,0,0,True, False, True)
        '''
        while True:
            try:
                if self.tile_list.currentItemChanged:
                    self.changeIcon()
            except:
                pass
        '''
        
        self.show()

    def level_select(self):
        self.windowl = QDialog(self)
        global levels
        self.levellist = QListWidget()
        self.levellist.setIconSize(QSize(200, 25))
        try:
            for i in range(levels):
                item = QListWidgetItem(QIcon("icons/level.jpg"),"Level "+str(i+1))
                self.levellist.addItem(item)
        except Exception as e:
            print(str(e))
            pass

        self.levellist.itemClicked.connect(lambda: self.change_level(False, False))
        self.layoutl = QHBoxLayout()
        self.layoutl.addWidget(self.levellist)
        self.windowl.setGeometry(150,150,400,300)
        self.windowl.setWindowTitle("Choose a level")
        self.windowl.setWindowIcon(QIcon("icons/icon.ico"))
        self.windowl.setLayout(self.layoutl)
        self.windowl.exec_()

    def change_level_new(self):
        global level
        self.file_save(True)
        level = self.levelSelect.currentIndex()
        self.file_open(True)

    def change_level(self, but = False, up = False, undo = False):
        global level, levels

        if not undo:
            templist = [(None,None,None,None,level)]
        
        if not but:
            self.file_save(True)
            level = int(self.levelSelect.currentIndex()) #+1 X First level should be 0
            print(level)
            self.file_open(True)
            try:
                self.windowl.close()
            except:
                pass
            #self.level.setText("Level: " + str(level+1))
        if up:
            self.file_save(True)
            if level != levels-1:
                level = int(level+1)
            else:
                pass
            print(level)
            self.file_open(True)
            #self.level.setText("Level: " + str(level+1))
        elif not up and but:
            self.file_save(True)
            if level != 0:
                level = int(level-1)
            else:
                pass
            print(level)
            self.file_open(True)
            #self.level.setText("Level: " + str(level+1))            
        #change grid to grid for level

        if not undo:
            templist.append((None,None,None,None,level))
            history.append(templist)
            
    def update_levels(self):
        try:
            for i in range(1000):
                try:
                    self.levelSelect.removeItem(i)
                except:
                    break
        except:
            pass
        print(levels)
        self.levelSelect.removeItem(0)
        for i in range(levels):
            self.levelSelect.addItem("Level %s" % str(i+1))

    def changeCurrentList(self):
        global current_list
        print("current list: tile_list%s" % str(self.list_tab_widget.currentIndex()+1))
        current_list = eval('self.tile_list%s' % str(self.list_tab_widget.currentIndex()+1))

    def rotateCW_func(self):
        global rotation
        if rotation < 3:
            rotation = rotation + 1
        else:
            rotation = 0
        self.changeIcon()

    def rotateCCW_func(self):
        global rotation
        if rotation == 0:
            rotation = 3
        else:
            rotation = rotation - 1
        self.changeIcon()

    def prefab_list_up(self):
        current_list = eval('self.tile_list%s' % str(self.list_tab_widget.currentIndex()+1))
        currentRow = self.current_list.currentRow()

        if currentRow > 0:
            currentItem = self.current_list.takeItem(currentRow)
            self.current_list.insertItem(currentRow - 1, currentItem)
            self.current_list.setCurrentRow(currentRow - 1)
            self.update_list_file(currentRow, currentRow - 1)
            self.changeIcon()

    def prefab_list_down(self):
        current_list = eval('self.tile_list%s' % str(self.list_tab_widget.currentIndex()+1))
        currentRow = self.current_list.currentRow()
        if currentRow < self.current_list.count() - 1:
            currentItem = self.current_list.takeItem(currentRow)
            self.current_list.insertItem(currentRow + 1, currentItem)
            self.current_list.setCurrentRow(currentRow + 1)
            self.update_list_file(currentRow, currentRow + 1)
            self.changeIcon()

    def update_list_file(self, old_index, new_index):

        #NEEDS TO BE REDONE
        
        file_list = ["prefab_template/prefab_list.txt", "prefab_template/prefab_icon_list.txt", "prefab_template/prefab_text_list.txt"]
        list_list = [prefab_list, prefab_icon_list, prefab_text_list]

        for l in list_list:
            l.insert(new_index, l.pop(old_index))

            with open(file_list[list_list.index(l)], "w") as file:

                if list_list.index(l) == 0:   
                    rot_file = open("prefab_template/rot_prefab_list.txt", "w")

                for item in l:
                    file.write(item + "\n")

                    if list_list.index(l) == 0: 
                        rot_file.write(item + "_icon_list.txt" + "\n")

        #stupid icon lists, making me add more lines of code to my already concise function
         

    def prefab_list_del(self, currentprefab):

        #NEEDS TO BE REDONE
        global current_list
        #print(currentprefab)
        index_list_index = 0
        if current_list == self.tile_list2: index_list_index = 1
        if current_list == self.tile_list3: index_list_index = 2
        #print(index_list_index)
        
        self.restartCheck = QCheckBox()
        self.restartCheck.setText("Restart after deletion?")

        choice = QMessageBox.question(self,"Delete Prefab (DO NOT DELETE STOCK PREFABS)","Are you sure you want to delete \"%s\"?\nThis is mainly for developers." %(prefab_text_list[self.list_tab_widget.currentIndex()][currentprefab]),
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
           
        if choice == QMessageBox.Yes:
            text_list = ['prefab_template/prefab_text_list.txt','prefab_template/rot_prefab_list.txt',
                 'prefab_template/prefab_list.txt', 'prefab_template/prefab_icon_list.txt']

            for cur in text_list:
                file = open(cur, 'r+')
                cur_list = file.readlines()
                file.seek(0)
                file.truncate()

                print(cur_list[index_section_list[self.list_tab_widget.currentIndex()]+currentprefab+1])
                del cur_list[index_section_list[self.list_tab_widget.currentIndex()]+currentprefab+1]
                cur_str = "".join(cur_list)
                file.write(cur_str)
                file.close()
            
            restart_btn = QPushButton("Restart")
            later_btn = QPushButton("Later")
            choice = QMessageBox(self)
            choice.setIcon(QMessageBox.Question)
            choice.setWindowTitle("Prefab Successfully Deleted")
            choice.setText("Program must be restarted for changes to take effect.")
            choice.setInformativeText("Restart? You will lose any unsaved progress.")
            choice.addButton(restart_btn, QMessageBox.YesRole)
            choice.addButton(later_btn, QMessageBox.NoRole)
            choice.setDefaultButton(later_btn)
                              
            if choice.exec_() == 0:
                try:
                    subprocess.Popen('EasyTF2Mapper.exe')
                except:
                    subprocess.Popen('python main.py')
                sys.exit()
            else:
                pass
            
        else:
            del choice

    def changeIcon(self):
        global rotation
        
        current_list = eval('self.tile_list%s' % str(self.list_tab_widget.currentIndex()+1))
        try:
            current_prefab_icon_list = rotation_icon_list[self.list_tab_widget.currentIndex()][current_list.currentRow()]
            current_prefab_icon_list = open('prefab_template/iconlists/'+current_prefab_icon_list, 'r+')
            current_prefab_icon_list = current_prefab_icon_list.readlines()
            icon = current_prefab_icon_list[rotation]
            if "\n" in icon:
                icon = icon[:-1]
            self.current.setIcon(QIcon(icon))
            self.current.setIconSize(QSize(32,32))
        except Exception as e:
            print(str(e))
            icon = prefab_icon_list[self.list_tab_widget.currentIndex()][current_list.currentRow()]
            self.current.setIcon(QIcon(icon))
            self.current.setIconSize(QSize(32,32))
        '''
        try:
            current_prefab_icon_list2 = open('prefab_template/rot_prefab_list.txt', 'r+')
            current_prefab_icon_list2 = current_prefab_icon_list2.readlines()
            current_prefab_icon_list2 = current_prefab_icon_list2[self.tile_list1.currentRow()]
            if "\n" in current_prefab_icon_list2:
                current_prefab_icon_list2 = current_prefab_icon_list2[:-1]
            current_prefab_icon_list2 = open('prefab_template/iconlists/'+current_prefab_icon_list2, 'r+')
            current_prefab_icon_list2 = current_prefab_icon_list2.readlines()
            icon2 = current_prefab_icon_list2[rotation]
            if "\n" in icon2:
                icon2 = icon2[:-1]
            self.current.setIcon(QIcon(icon2))
            self.current.setIconSize(QSize(32,32))
        except Exception as e:
            print(str(e))
            icon = prefab_icon_list[self.tile_list1.currentRow()]
            self.current.setIcon(QIcon(icon))
            self.current.setIconSize(QSize(32,32))


        #might consider using the following code in the future    
        
        im_rot = Image.open(prefab_icon_list[self.tile_list.currentRow()])
        im_rot = im_rot.rotate(360-(rotation*90))
        data = im_rot.tobytes('raw')#('raw', 'RGBA')
        im_rot_qt = QImage(data, im_rot.size[0], im_rot.size[1], QImage.Format_ARGB32)
        im_rot.close()
        icon = QPixmap.fromImage(im_rot_qt)
        self.current.setIcon(QIcon(icon))
        self.current.setIconSize(QSize(32,32))
        '''             
        

 
        
        
    def file_open(self, tmp = False, first = False):
        global grid_list, iconlist, level, stored_info_list, totalblocks,entity_list, currentfilename, file_loaded, latest_path,save_dict,load_dict
        print(latest_path)
        if not tmp:
            name = QFileDialog.getOpenFileName(self, "Open File", latest_path,"*.ezm")
            latest_path,file = str(name[0]),open(name[0], "rb")
            level = 0
            iconlist=[]
            while True:
                header = pickle.load(file)
                if "levels" in header:
                    openlines = pickle.load(file)
                    levelcountload = openlines
                    
                elif "grid_size" in header:
                    openlines = pickle.load(file)
                    self.grid_change(openlines[0],openlines[1],openlines[2],False, True, True)
                elif "stored_info_list" in header:
                    stored_info_list=[]
                    stored_info_list_temp=[]
                    openlines = pickle.load(file)
                    for item in openlines:
                        stored_info_list_temp.append(item)
                    for index,lvl in enumerate(stored_info_list_temp):
                        stored_info_list.append([])
                        for info in lvl:
                            try:
                                temp = save_dict[info[0]]
                                info[0] = temp
                                stored_info_list[index].append(info)
                            except:
                                stored_info_list[index].append('')
                elif "icon_list" in header:
                    global grid_list
                    iconlist=[]
                    openlines = pickle.load(file)

                    for item in openlines:
                        iconlist.append(item)
                    for index, icon in enumerate(iconlist[0]):
                        if "icons" in icon:
                            grid_list[index].button.setIcon(QIcon(icon))
                            grid_list[index].button.setIconSize(QSize(32,32))
                elif "skybox2_list" in header:
                    openlines = pickle.load(file)
                    skybox2_list.setCurrentRow(openlines)
                else:
                    break
        
            for i in range(levelcountload):
                file = open("leveltemp/level" + str(i)+".tmp", "wb")
                pickle.dump(iconlist[i], file)
                file.close()
              
            self.change_skybox()
            file.close()
            self.setWindowTitle("Easy TF2 Mapper - [" + str(name[0]) + "]")
            currentfilename = str(name[0])
            file_loaded = True
            
        else:
            try:
                file = open("leveltemp/level" + str(level)+".tmp", "rb")
                iconlist[level] = pickle.load(file)
                file.close()
                for index, icon in enumerate(iconlist[level]):
                    grid_list[index].button.setIcon(QIcon(icon))
                    grid_list[index].button.setIconSize(QSize(32,32))
            except Exception as e:
                print(str(e))
            
    def file_save(self, tmp = False, saveAs = False):
        global grid_x, grid_y, iconlist, levels, level, currentfilename, file_loaded, latest_path, stored_info_list, save_dict,load_dict,skybox2_list
        print(latest_path)
        gridsize_list = (grid_x,grid_y,levels)
        try:
            skybox_sav = skybox2_list.currentRow()
        except:
            pass
        if not tmp:
            if not file_loaded or saveAs:
                name = QFileDialog.getSaveFileName(self, "Save File", latest_path, "*.ezm")[0]
                latest_path = name
            else:
                if "*" in currentfilename:
                    name = currentfilename[:-1]
                else:
                    name = currentfilename
            file = open(name, "wb")
            pickle.dump("<levels>",file)
            pickle.dump(levels,file)
            pickle.dump("<grid_size>", file)
            pickle.dump(gridsize_list, file)
            pickle.dump("<stored_info_list>", file)
            stored_info_list_temp=[]
            for index,lvl in enumerate(stored_info_list):
                stored_info_list_temp.append([])
                for info in lvl:
                    print(info)
                    try:
                        temp = load_dict[info[0]]
                        info[0] = temp
                        stored_info_list_temp[index].append(info)
                    except:
                        stored_info_list_temp[index].append('')
            pickle.dump(stored_info_list_temp, file)
            pickle.dump("<icon_list>", file)
            pickle.dump(iconlist, file)
            pickle.dump("<skybox>", file)
            pickle.dump(skybox_sav, file)
            file.close()
            QMessageBox.information(self, "File Saved", "File saved as %s" %(name))

            self.setWindowTitle("Easy TF2 Mapper - [" + name + "]")

            currentfilename = name
            file_loaded = True
        else:
            try:#writes tmp file to save the icons for each level
                file = open("leveltemp/level" + str(level)+".tmp", "wb")
                pickle.dump(iconlist[level], file)
                file.close()
            except Exception as e:
                
                print(str(e))
        
        

    def file_export(self,bsp=False):
        global cur_vmf_location,id_num,stored_info_list, grid_y, grid_x, world_id_num, count_btns, currentlight, skybox, skybox2_list, entity_list, skybox_light_list, skybox_angle_list, latest_path
        skyboxgeolist = []
        skyboxz = QInputDialog.getText(self,("Set Skybox Height"),("Skybox Height(hammer units, %d minimum recommended):" %(levels*512)), QLineEdit.Normal, "%d" %(levels*512))
        try:
            skyboxz = int(skyboxz[0])
        except:
            QMessageBox.critical(self, "Error", "Please enter a number.")
            if bsp == False:
                self.file_export()
            else:
                self.file_export(True)
        #generate skybox stuff now
        create = generateSkybox.createSkyboxLeft(grid_x,grid_y,skyboxz,id_num,world_id_num)
        skyboxgeolist.append(create[0])
        id_num = create[1]
        world_id_num = create[2]
        create = generateSkybox.createSkyboxNorth(grid_x,grid_y,skyboxz,id_num,world_id_num)
        skyboxgeolist.append(create[0])
        id_num = create[1]
        world_id_num = create[2]
        create = generateSkybox.createSkyboxRight(grid_x,grid_y,skyboxz,id_num,world_id_num)
        skyboxgeolist.append(create[0])
        id_num = create[1]
        world_id_num = create[2]
        create = generateSkybox.createSkyboxTop(grid_x,grid_y,skyboxz,id_num,world_id_num)
        skyboxgeolist.append(create[0])
        id_num = create[1]
        world_id_num = create[2]
        create = generateSkybox.createSkyboxSouth(grid_x,grid_y,skyboxz,id_num,world_id_num)
        skyboxgeolist.append(create[0])
        skybox = skybox_list[skybox2_list.currentRow()]
        skyboxlight = skybox_light_list[skybox2_list.currentRow()]
        skyboxangle = skybox_angle_list[skybox2_list.currentRow()]

        try:
            currentlight = currentlight.replace("world_idnum",str(world_id_num))
            currentlight = currentlight.replace("CURRENT_LIGHT",skyboxlight)
            currentlight = currentlight.replace("CURRENT_ANGLE",skyboxangle)
        except:
            QMessageBox.critical(self, "Error", "Please choose a skybox.")
            self.change_skybox()
        light = currentlight
        latest_path = latest_path.replace(".ezm",".vmf")
        if not bsp:
            name = QFileDialog.getSaveFileName(self, "Export .vmf", latest_path, "Valve Map File (*.vmf)")
            file = open(name[0], "w+")
            totalblocks =[]
            entity_list=[]
            for lvl in stored_info_list:
                for prfb in lvl:
                    if prfb != '':
                        try:
                            try:
                                try:
                                    try:
                                        create = prfb[0].createTile(prfb[1], prfb[2], prfb[3], prfb[4], prfb[5], prfb[6], prfb[7], prfb[8])
                                    except Exception as e:
                                        create = prfb[0].createTile(prfb[1], prfb[2], prfb[3], prfb[4], prfb[5], prfb[6], prfb[7], prfb[8])
                                except Exception as e:
                                    create = prfb[0].createTile(prfb[1], prfb[2], prfb[3], prfb[4], prfb[8])
                            except Exception as e:
                                create = prfb[0].createTile(prfb[1], prfb[2], prfb[3], prfb[4], prfb[5], prfb[6], prfb[8])
                        except Exception as e:
                            create = prfb[0].createTile(prfb[1], prfb[2], prfb[3], prfb[4], prfb[7], prfb[8])
                        id_num = create[1]
                        world_id_num = create[2]
                        totalblocks.append(create[0])
                        try:
                            entity_num = create[3]
                            placeholder_list = create[5]
                        except IndexError:
                            pass
                        try:
                            entity_list.append(create[4])
                        except Exception as e:
                            print(str(e))
            import export
            wholething = export.execute(totalblocks, entity_list, levels, skybox,skyboxgeolist, light)
            file.write(wholething)
            file.close()
            popup = QMessageBox(self, "File Exported",
                                    "The .vmf has been outputted to %s" %(name[0]) + " Open it in hammer to compile as a .bsp. Check out the wiki (https://github.com/baldengineers/easytf2_mapper/wiki/Texture-bug) for fixing errors with textures.")
            popup.setWindowTitle("File Exported")
            popup.setText("The .vmf has been outputted to %s" %(name[0]))
            popup.setInformativeText(" Open it in hammer to compile as a .bsp and/or make some changes.")
            hammerButton = popup.addButton("Open Hammer",QMessageBox.ActionRole)
            exitButton = popup.addButton("OK",QMessageBox.ActionRole)
            popup.exec_()
            if popup.clickedButton() == hammerButton:
                self.open_hammer(1,name[0])
            if popup.clickedButton() == exitButton:
                popup.deleteLater()
            cur_vmf_location = name[0]
        else:
            file = open('output/tf2mapperoutput.vmf','w+')
            totalblocks =[]
            entity_list=[]
            for lvl in stored_info_list:
                for prfb in lvl:
                    if prfb != '':
                        try:
                            try:
                                try:
                                    try:
                                        create = prfb[0].createTile(prfb[1], prfb[2], prfb[3], prfb[4], prfb[5], prfb[6], prfb[7], prfb[8])
                                    except Exception as e:
                                        create = prfb[0].createTile(prfb[1], prfb[2], prfb[3], prfb[4], prfb[5], prfb[6], prfb[7], prfb[8])
                                except Exception as e:
                                    create = prfb[0].createTile(prfb[1], prfb[2], prfb[3], prfb[4], prfb[8])
                            except Exception as e:
                                create = prfb[0].createTile(prfb[1], prfb[2], prfb[3], prfb[4], prfb[5], prfb[6], prfb[8])
                        except Exception as e:
                            create = prfb[0].createTile(prfb[1], prfb[2], prfb[3], prfb[4], prfb[7], prfb[8])
                        id_num = create[1]
                        world_id_num = create[2]
                        totalblocks.append(create[0])
                        try:
                            entity_num = create[3]
                            placeholder_list = create[5]
                        except IndexError:
                            pass
                        try:
                            entity_list.append(create[4])
                        except Exception as e:
                            print(str(e))
            import export
            wholething = export.execute(totalblocks, entity_list, levels, skybox,skyboxgeolist, light)
            file.write(wholething)
            file.close()
            cur_vmf_location = 'output/tf2mapperoutput.vmf'

        
        
    def file_export_bsp(self):
        global cur_vmf_location
        self.file_export(True)
        try:
            tf2BinLoc = open('startupcache/vbsp.su','r+')
            tf2BinLocFile = tf2BinLoc.readlines()[0].replace('\\','/')
            tf2BinLoc.close()
            subprocess.call('"'+tf2BinLocFile+'/vbsp.exe" "'+cur_vmf_location+'"')
            subprocess.call('"'+tf2BinLocFile+'/vvis.exe" '+cur_vmf_location.replace('.vmf','.bsp')+'"')
            subprocess.call('"'+tf2BinLocFile+'/vrad.exe" '+cur_vmf_location.replace('.vmf','.bsp')+'"')
            shutil.copyfile(cur_vmf_location.replace('.vmf','.bsp'),tf2BinLocFile.replace('/bin','/tf/maps/tf2mapperoutput.bsp'))
            popup = QMessageBox(self)
            popup.setWindowTitle("File Exported")
            popup.setText("The .vmf has been outputted to %s" %(tf2BinLocFile.replace('/bin','/tf/maps/tf2mapperoutput.bsp')))
            popup.setInformativeText("Open TF2 and in load up 'tf2mapperoutput.bsp'! You can do this by typing 'map tf2mapperoutput' or by creating a server with that map.\n\nThere also is a .vmf file of your map stored in output/tf2mapperoutput.vmf.")
            hammerButton = popup.addButton("Open TF2",QMessageBox.ActionRole)
            exitButton = popup.addButton("OK",QMessageBox.ActionRole)
            popup.exec_()
            if popup.clickedButton() == hammerButton:
                subprocess.Popen('"'+tf2BinLocFile.replace('steamapps/common/Team Fortress 2/bin','')+'steam.exe" "steam://run/440"')
            if popup.clickedButton() == exitButton:
                popup.deleteLater()            
            

            
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            try:
                tf2BinLoc = open('startupcache/vbsp.su', 'w+')
                tf2BinLocFile = QFileDialog.getExistingDirectory(self,'LOCATE Team Fortress 2/bin, NOT IN DEFAULT LOCATION!')
                tf2BinLocFile = str(tf2BinLocFile.replace('\\','/'))
                tf2BinLoc.write(tf2BinLocFile)
                tf2BinLoc.close()
                subprocess.call('"'+tf2BinLocFile+'/vbsp.exe" "'+cur_vmf_location+'"')
                subprocess.call('"'+tf2BinLocFile+'/vvis.exe" "'+cur_vmf_location.replace('.vmf','.bsp')+'"')
                subprocess.call('"'+tf2BinLocFile+'/vrad.exe" "'+cur_vmf_location.replace('.vmf','.bsp')+'"')
                shutil.copyfile(cur_vmf_location.replace('.vmf','.bsp'),tf2BinLocFile.replace('/bin','/tf/maps/tf2mapperoutput.bsp'))
                popup = QMessageBox(self)
                popup.setWindowTitle("File Exported")
                popup.setText("The .vmf has been outputted to %s" %(tf2BinLocFile.replace('/bin','/tf/maps/tf2mapperoutput.bsp')))
                popup.setInformativeText("Open TF2 and in load up 'tf2outputmapper.bsp'! You can do this by typing 'map tf2mapperoutput' or by creating a server with that map.\n\nThere also is a .vmf file of your map stored in output/tf2mapperoutput.vmf.")
                hammerButton = popup.addButton("Open TF2",QMessageBox.ActionRole)
                exitButton = popup.addButton("OK",QMessageBox.ActionRole)
                popup.exec_()
                if popup.clickedButton() == hammerButton:
                    subprocess.Popen('"'+tf2BinLocFile.replace('steamapps/common/Team Fortress 2/bin','')+'steam.exe" "steam://run/440"')
                if popup.clickedButton() == exitButton:
                    popup.deleteLater()
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                QMessageBox.critical(self, "Error", "Something went wrong while exporting!")
                

            
    def removeButtons(self):

        for i in reversed(range(self.button_grid_layout.count())):
            widget = self.button_grid_layout.takeAt(i).widget()

            if widget is not None:
                widget.deleteLater()
        
    def grid_change(self,xvar,yvar,zvar,var,var2,var3):
        global totalblocks,entity_list,grid_list,iconlist
        if var2 == True:
            sxvar = xvar
            syvar = yvar
            szvar = zvar
        else:
            pass
        self.count = 0
        count_btns=0
        if var3 == True:
            try:
                del entity_list
                del totalblocks
                del iconlist
                del grid_list
                entity_list = []
                iconlist = []
                totalblocks = []
                grid_list = []
            except Exception as e:
                print(str(e))
                pass

        #gridsize_list = []
        self.btn_id_count = 0
        if var == True:
            self.window = QDialog(self)

            self.text = QLineEdit()
            self.text2 = QLineEdit()
            self.text3 = QLineEdit()

            self.okay_btn = QPushButton("OK",self)
            self.okay_btn.clicked.connect(lambda: self.grid_change_func(self.text.displayText(), self.text2.displayText(), self.text3.displayText()))

            self.form = QFormLayout()
            self.form.addRow("Set Grid Width:",self.text)
            self.form.addRow("Set Grid Height:",self.text2)
            self.form.addRow("Set Amount of Levels:",self.text3)
            self.form.addRow(self.okay_btn)

            self.window.setLayout(self.form)
            self.window.setWindowTitle("Set Grid Size")
            self.window.exec_()
        elif var2 == True:
            self.grid_change_func(sxvar,syvar,szvar)

    def grid_change_func(self,x,y,z):
        global grid_y, grid_x, levels, file_loaded, currentfilename, level, count_btns
        level = 0
        levels = 1
        count_btns = 0
        self.count = 0
        
        file_loaded = False
        try:
            self.window.deleteLater()
        except:
            pass

        try:
            self.grid_y = int(y)
            self.grid_x = int(x)
            levels = int(z)
        except ValueError:
            #TODO: Instead of a print statement, we need to bring up a window, alerting the user
            QMessageBox.critical(self.window, "Error", "Please enter a number.")
            self.grid_change(0,0,0,False,False,True)

        self.removeButtons()

        for z in range(levels):
            totalblocks.append([])
            entity_list.append([])
            iconlist.append([])
            stored_info_list.append([])
            self.btn_id_count=0
            count_btns=0
        
            for x in range(self.grid_x):
                
                for y in range(self.grid_y):
                    totalblocks[z].append("") #This is so that there are no problems with replacing list values
                    
                    
                    count_btns += 1
                    entity_list[z].append("")
                    iconlist[z].append("")
                    stored_info_list[z].append('')
        for x in range(self.grid_x):
            for y in range(self.grid_y):
                grid_btn = GridBtn(self, x, y, self.btn_id_count)
                self.button_grid_layout.addWidget(grid_btn.button,y,x)
                self.btn_id_count += 1
                grid_list.append(grid_btn)
        entity_list.append("lighting slot")  
        self.count += 1
        count_btns = self.grid_x*self.grid_y
        grid_y = self.grid_y
        grid_x = self.grid_x

        self.scrollArea.deleteLater()
        self.scrollArea = QScrollArea()
        self.scrollArea.setBackgroundRole(QPalette.Light)
        self.scrollArea.setStyleSheet("background-color: rgb(50, 50, 50, 100);")


        self.grid_widget = QWidget()
        self.grid_widget.setLayout(self.button_grid_layout)
        self.scrollArea.setWidget(self.grid_widget)
        self.scrollArea.ensureWidgetVisible(self.grid_widget)
        self.scrollArea.setWidgetResizable(True)
        
        self.button_grid_layout.setRowStretch(self.grid_y + 1, 1)
        self.button_grid_layout.setColumnStretch(self.grid_x + 1, 1)

        for i in range(levels):
            file = open("leveltemp/level" + str(i)+".tmp", "wb")
            pickle.dump(iconlist[i], file)
            file.close()
        
        self.gridLayout.addWidget(self.scrollArea)
        self.button_grid_all.addLayout(self.gridLayout)
        self.setWindowTitle("Easy TF2 Mapper ")

        self.update_levels()
        
        return grid_list

    def change_light(self):
        global r_input, g_input, b_input, light_input, world_id_num
        
        r_input = QInputDialog.getText(self, ("Red light level 0-255"),
                                       ("Put in the red light ambiance level, 0-255:"))
        g_input = QInputDialog.getText(self, ("Green light level 0-255"),
                                       ("Put in the green light ambiance level, 0-255:"))
        b_input = QInputDialog.getText(self, ("Blue light level 0-255"),
                                       ("Put in the blue light ambiance level, 0-255:"))
        light_input = QInputDialog.getText(self, ("Brightness level"),
                                       ("Put in the brightness level desired:"))
        try:
            
            r_input = int(r_input[0])
            g_input = int(g_input[0])
            b_input = int(b_input[0])
            light_input = int(light_input[0])
            if r_input > 255 or g_input > 255 or b_input > 255:
                print("Error. Put in a number below 256 for each color input")
            else:
                pass
        except ValueError:
            QMessageBox.critical(self, "Error", "Please enter a number.")
            self.change_light()

        global currentlight
        currentlight = light_create.replacevalues(r_input,g_input,b_input,light_input,world_id_num)

    def change_skybox(self):
        self.window = QDialog(self)
        global skybox2_list
        skybox2_list = QListWidget()
        skybox2_list.setIconSize(QSize(200, 25))
        for index, text in enumerate(skybox_list):
            item = QListWidgetItem(QIcon(skybox_icon_list[index]), text)
            skybox2_list.addItem(item)
        
        self.layout = QHBoxLayout()
        self.layout.addWidget(skybox2_list)
        self.window.setGeometry(150,150,400,300)
        self.window.setWindowTitle("Choose a skybox")
        self.window.setWindowIcon(QIcon("icons\icon.ico"))

        self.window.setLayout(self.layout)
        skybox2_list.itemClicked.connect(self.window.close)
        self.window.exec_()
    '''
    def importprefabs(self):
        prefab_text_list = []
        prefab_icon_list = []
        prefab_list=[]
        prefab_file = open("prefab_template\prefab_list.txt")
        prefab_text_file = open("prefab_template\prefab_text_list.txt")
        prefab_icon_file = open("prefab_template\prefab_icon_list.txt")
        for line in prefab_file.readlines():
            prefab_list.append(line[:-1] if line.endswith("\n") else line)# need to do this because reading the file generates a \n after every line

        for line in prefab_text_file.readlines():
            prefab_text_list.append(line[:-1] if line.endswith("\n") else line)

        for line in prefab_icon_file.readlines():
            prefab_icon_list.append(line[:-1] if line.endswith("\n") else line)

        for file in [prefab_file, prefab_text_file, prefab_icon_file]:
            file.close()
        for item in prefab_list:
            globals()[item] = importlib.import_module(item)
            print("import", item)
        self.home()
    '''
    #fix this later, it has a breaking bugs if it works

    def close_application(self, restart = False):
        if not restart:
            close = True
            
            if "*" in self.windowTitle():
                print('are you sure')
                choice = QMessageBox.warning(self, "Exit TF2Mapper",
                                              "Some changes have not been saved.\nDo you really want to quit?",
                                              QMessageBox.Ok | QMessageBox.Cancel,
                                              QMessageBox.Cancel)
                if choice != QMessageBox.Ok:
                    close = False
                
            if close:
                folder = 'leveltemp/'
                for f in os.listdir(folder):
                    if "level" in f: 
                        print("removing", f)
                        os.remove(folder+f)
                    
                sys.exit()
            else:
                pass
        if restart:
            choice = QMessageBox.question(self, "Restart",
                                          "Are you sure you want to restart?",
                                          QMessageBox.Yes | QMessageBox.No,
                                          QMessageBox.No)
            if choice == QMessageBox.Yes:
                folder = 'leveltemp/'
                for f in os.listdir(folder):
                    if "level" in f: 
                        print("removing", f)
                        os.remove(folder+f)
                    
                try:
                    subprocess.call('sudo wine EasyTF2Mapper.exe')
                    
                except:
                    try:
                        subprocess.Popen('EasyTF2Mapper.exe')
                    except:
                        subprocess.Popen('python main.py')
                sys.exit()
            else:
                pass

    def create_prefab(self):
        
        self.window = QDialog(self)
        self.textLineEdit = QLineEdit()
        self.nameLineEdit = QLineEdit()
        
        self.vmfTextEdit = QLineEdit()
        self.iconTextEdit = QLineEdit()
        
        self.vmfBrowse = QPushButton("Browse",self)
        self.vmfBrowse.clicked.connect(lambda: self.vmfTextEdit.setText(QFileDialog.getOpenFileName(self, "Choose .vmf File", "/","*.vmf")[0]))
        
        self.iconBrowse = QPushButton("Browse",self)
        self.iconBrowse.clicked.connect(lambda: self.iconTextEdit.setText(QFileDialog.getOpenFileName(self, "Choose .jpg File", "/","*.jpg")[0]))

        self.vmfLayout = QHBoxLayout()
        self.vmfLayout.addWidget(self.vmfTextEdit)
        self.vmfLayout.addWidget(self.vmfBrowse)
        self.vmfBrowse.setWindowModality(Qt.NonModal)
        
        self.iconLayout = QHBoxLayout()
        self.iconLayout.addWidget(self.iconTextEdit)
        self.iconLayout.addWidget(self.iconBrowse)

        self.okay_btn = QPushButton("Create Prefab", self)

        self.blankstring = QWidget()

        self.okay_btn_layout = QHBoxLayout()
        self.okay_btn_layout.addStretch(1)
        self.okay_btn_layout.addWidget(self.okay_btn)

        self.okay_btn.clicked.connect(self.create_run_func)

        self.rotCheckBox = QCheckBox()
        self.expCheckBox = QCheckBox()
        self.buggyText = QLabel("This is a pretty buggy tool at this point, and is mostly used by developers. Are you sure you want to do this? \n(exported prefabs can be found in the main directory, where the executable is.)")

        self.sectionSelect = QComboBox()
        self.sectionSelect.addItems(["Geometry","Map Layout","Fun/Other"])
        
        self.form = QFormLayout()
        self.form.addRow(self.buggyText)
        self.form.addRow("Prefab Text:", self.textLineEdit)
        self.form.addRow("Prefab Name:", self.nameLineEdit)
        self.form.addRow("VMF file (.vmf):", self.vmfLayout)
        self.form.addRow("Icon (.jpg):", self.iconLayout)
        self.form.addRow("Make Rotations?", self.rotCheckBox)
        self.form.addRow("Export prefab?", self.expCheckBox)
        self.form.addRow("Which section?",self.sectionSelect)
        for i in range(5):
            self.form.addRow(self.blankstring)
        self.form.addRow(self.okay_btn_layout)

        
        self.window.setGeometry(150,150,400,300)
        self.window.setWindowTitle("Create Prefab")
        self.window.setWindowIcon(QIcon("icons\icon.ico"))

        self.window.setLayout(self.form)
        self.window.exec_()

    def create_run_func(self):
        if self.sectionSelect.currentIndex() == 2:
            input_number = 'END'
        else:
            input_number = index_section_list[self.sectionSelect.currentIndex()+1]
        name_str = self.nameLineEdit.displayText().replace(' ','_')
        form_list,t_list = [self.vmfTextEdit.displayText(),self.textLineEdit.displayText(),self.iconTextEdit.displayText(),self.nameLineEdit.displayText()],[]
        form_dict = {1:'Prefab Text',2:'Prefab Name',3:'VMF file',4:'Icon'}
        if self.vmfTextEdit.displayText() !=  '' and self.textLineEdit.displayText() != '' and self.iconTextEdit.displayText() != '' and self.nameLineEdit.displayText() != '':
            QMessageBox.information(self, "Files Created, restart to see the prefab.",
                                                                          createPrefab.create(self.vmfTextEdit.displayText(), name_str,
                                                                            self.textLineEdit.displayText(), self.iconTextEdit.displayText(),
                                                                                self.rotCheckBox.isChecked(),self.expCheckBox.isChecked(),input_number,self.sectionSelect.currentIndex()))
            restart_btn = QPushButton("Restart")
            later_btn = QPushButton("Later")
            choice = QMessageBox(self)
            choice.setIcon(QMessageBox.Question)
            choice.setWindowTitle("Prefab Successfully Created")
            choice.setText("Program must be restarted for changes to take effect.")
            choice.setInformativeText("Restart? You will lose any unsaved progress.")
            choice.addButton(restart_btn, QMessageBox.YesRole)
            choice.addButton(later_btn, QMessageBox.NoRole)
            choice.setDefaultButton(later_btn)                
            if choice.exec_() == 0:
                try:
                    subprocess.call('sudo wine EasyTF2Mapper.exe')
                    
                except:
                    try:
                        subprocess.Popen('EasyTF2Mapper.exe')
                    except:
                        subprocess.Popen('python main.py')
                sys.exit()
            else:
                pass  
        else:
            for index,box in enumerate(form_list):         
                if box == '':          
                    t_list.append(form_dict[index+1])
            err = ", ".join(t_list)
            QMessageBox.critical(self, "Error", "Fill out all sections of the form. ("+err+")")
        #self.importprefabs()

    def import_prefab(self):
        name = QFileDialog.getOpenFileName(self, "Import Zipped Prefab", latest_path,"*.zip")[0]
        prefab_zip = zipfile.ZipFile(name).extractall("")

        with open("info.txt", "r+") as f:
            zip_info = f.readlines()
            if zip_info[3] == 2:
                with open('prefab_template/rot_prefab_list.txt',"a") as d:
                    tempfil = zip_info[0]
                    tempfil = tempfil.replace('\n','')
                    d.write(tempfil+"_icon_list.txt\n")
                with open('prefab_template/prefab_list.txt',"a") as d:
                    tempfil = zip_info[0]
                    tempfil = tempfil.replace('\n','')
                    d.write(tempfil+'\n')
                with open('prefab_template/prefab_text_list.txt',"a") as d:
                    d.write(zip_info[2])
                with open('prefab_template/prefab_icon_list.txt',"a") as d:
                    tempfil = zip_info[1]
                    tempfil = tempfil.replace('\n','')
                    d.write('icons/'+tempfil+'_right.jpg\n')
            else:
                #most childish code 2016
                z = open('prefab_template/rot_prefab_list.txt',"r")
                zlines = z.readlines()
                z.close()
                y = open('prefab_template/prefab_list.txt',"r")
                ylines = y.readlines()
                y.close()
                x = open('prefab_template/prefab_text_list.txt',"r")
                xlines = x.readlines()
                x.close()
                w = open('prefab_template/prefab_icon_list.txt',"r")
                wlines = w.readlines()
                w.close()
                
                z = open('prefab_template/rot_prefab_list.txt',"w")
                zlines.insert(self.index_section_index[int(zip_info[3])]-1,zip_info[0]+"_icon_list.txt\n")
                zlines = "".join(zlines)
                z.write(zlines)
                z.close()
                y = open('prefab_template/prefab_list.txt',"w")
                ylines.insert(self.index_section_index[int(zip_info[3])]-1,zip_info[0])
                ylines = "".join(ylines)
                y.write(ylines)
                y.close()
                x = open('prefab_template/prefab_text_list.txt',"w")
                xlines.insert(self.index_section_index[int(zip_info[3])]-1,zip_info[2])
                xlines = "".join(xlines)
                x.write(xlines)
                x.close()
                w = open('prefab_template/prefab_icon_list.txt',"w")
                wlines.insert(self.index_section_index[int(zip_info[3])]-1,'icons/'+zip_info[1]+'_right.jpg\n')
                wlines = "".join(wlines)
                w.write(wlines)
                w.close()                

        os.remove("info.txt")
        
        restart_btn = QPushButton("Restart")
        later_btn = QPushButton("Later")
        choice = QMessageBox(self)
        choice.setIcon(QMessageBox.Question)
        choice.setWindowTitle("Prefab Successfully Imported")
        choice.setText("Program must be restarted for changes to take effect.")
        choice.setInformativeText("Restart? You will lose any unsaved progress.")
        choice.addButton(restart_btn, QMessageBox.YesRole)
        choice.addButton(later_btn, QMessageBox.NoRole)
        choice.setDefaultButton(later_btn)                 
        if choice.exec_() == 0:
            try:
                subprocess.call('sudo wine EasyTF2Mapper.exe')
            except:
                try:
                    subprocess.Popen('EasyTF2Mapper.exe')
                except:
                    subprocess.Popen('python main.py')
            sys.exit()
        else:
            pass  
        

    def open_console(self):
        #contains dev console where you can manually run functions

        self.console = QDialog()
        self.console.setWindowTitle("Developer Console")

        self.prev_text = QTextEdit("<Bald Engineers Developer Console>")
        self.prev_text.setText('''Developer console for Easy TF2 Mapper version r 1.0.1. Current commands are:
print <variable>, setlevel <int>, help, restart, exit, func <function>, wiki, py <python function>.\n''')
        self.prev_text.setReadOnly(True)
        
        self.curr_text = QLineEdit()
        self.curr_text_btn = QPushButton("Enter")
        self.curr_text_btn.clicked.connect(self.console_enter)
        
        self.curr_text_layout = QHBoxLayout()
        self.curr_text_layout.addWidget(self.curr_text)
        self.curr_text_layout.addWidget(self.curr_text_btn)
        
        self.console_close_btn = QPushButton("Close")
        self.console_close_btn.clicked.connect(self.console.close)
        
        self.console_form = QFormLayout()
        self.console_form.addRow(self.prev_text)
        self.console_form.addRow(self.curr_text_layout)
        self.console_form.addRow(self.console_close_btn)

        
        self.console.setLayout(self.console_form)
        self.console.show()

    def console_enter(self):
        global level, levels
        
        command = ""
        char_num = 0
        text = self.curr_text.displayText()
        text_prefix = text + " --> "
        
        command = text.split()[0]
        
        try:
            value = text.split()[1]
        except IndexError:
            value = ""

        if command == "print":

            try:
                new_text = text_prefix + str(eval(value))
            except Exception as e:
                new_text = text_prefix + str(e)

        elif command == "setlevel":
            try:
                if int(value)-1 < int(levels):
                    level = int(value)-1
                    self.level.setText("Level: " + str(level+1))
                    new_text = text_prefix + "Level set to "+str(value+".")
                else:
                    new_text = text_prefix + "Level "+str(value+" is out of range.")
            except Exception as e:
                new_text = text_prefix + str(e)

        elif command == "help":
            new_text = text_prefix + '''Developer console for Easy TF2 Mapper version r 1.0.1. Current commands are: print <variable>, func <function>, setlevel <int>, help, restart, exit, func <function>, wiki, py <python function>'''

        elif command == "exit":
            self.close_application()
            
        elif command == "restart":
            self.close_application(True)

        elif command == "pootis":
            new_text = '<img src="icons/thedoobs.jpg">'

        elif command == "sterries" or command == "jerries":
            new_text = text_prefix + "Gimme all those berries, berries, berries!"
            

        elif command == "sideshow":
            new_text = ''
            self.sideshow()
        elif command == "func":
            try:
                eval("self."+value + "()")
                new_text = text_prefix + "Function "+value+" has been run."
            except Exception as e:
                new_text = text_prefix + str(e)

        elif command == "wiki":
            try:
                webbrowser.open("http://github.com/baldengineers/easytf2_mapper/wiki")
                new_text = text_prefix + "Wiki has been opened in your default browser"
            except Exception as e:
                print(str(e))
                
        elif command == "py":
            try:
                new_text = text_prefix + str(eval(value))
            except Exception as e:
                new_text = text_prefix + str(e)
        else:
            new_text = text_prefix + "\"" + command + "\" is not a valid command"

        self.prev_text.append(new_text)
        self.curr_text.setText("")

    def undo(self, undo):
        if history if undo else redo_history:
            x = history[-1][0][0] if undo else redo_history[-1][1][0]
            y = history[-1][0][1] if undo else redo_history[-1][1][1]
            h_moduleName = history[-1][0][2] if undo else redo_history[-1][1][2]
            h_icon = history[-1][0][3] if undo else redo_history[-1][1][3]
            h_level = history[-1][0][4] if undo else redo_history[-1][1][4]

            if h_level == None:   
                for button in grid_list:
                    if button.x == x and button.y == y:
                        button.click_func(self, x, y, button.btn_id, False, h_moduleName, h_icon)
                        break
            else:
                self.level.setText("Level: " + str(h_level+1))
                self.levellist.setCurrentRow(h_level)
                self.change_level(False, False, True)

            redo_history.append(history.pop(-1)) if undo else history.append(redo_history.pop(-1))
        else:
            winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
        
        #format | click_func(parent, x, y, btn_id, clicked=True, h_moduleName="None", h_icon='')
        #format | history.append((x,y,moduleName,self.icon,level), (x,y,moduleName,self.icon,level))

    def sideshow(self):
        self.gif("icons/sideshow.gif", (350,262,154,103), "SIDESHOW", "icons/ss.ico")

    def heavy(self):
        self.gif("icons/heavy.gif", (350,262,150,99), "DANCE HEAVY DANCE!")

    def gif(self, file, geo, title, icon="icons\icon.ico"):
        self.gif = QLabel()
        movie = QMovie(file)
        self.gif.setMovie(movie)
        self.gif.setGeometry(geo[0],geo[1],geo[2],geo[3])
        self.gif.setWindowTitle(title)
        self.gif.setWindowIcon(QIcon(icon))
        self.gif.show()

        movie.start()

#define some global variables
level = 0
levels = 0
id_num = 1
rotation = 0
world_id_num = 2
entity_num = 1
btn_id_count = 0
grid_list=[]
totalblocks = []
skybox_list=[]
last_tuple = 'First'
skybox_light_list=[]
iconlist = []
rotation_icon_list=[]
skybox_angle_list=[]
skybox_icon_list=[]
prefab_list = []
gridsize_list = []
count_btns = 0
entity_list=[]

save_dict={}
load_dict={}

stored_info_list=[]

prefab_text_list = []
prefab_icon_list = []
openblocks=[]
placeholder_list = []
history = []
redo_history = []
currentfilename='Untitled'
file_loaded = False
current_loaded = ''
latest_path='/'
currentlight = '''
entity
{
    "id" "world_idnum"
    "classname" "light_environment"
    "_ambient" "255 255 255 100"
    "_ambientHDR" "-1 -1 -1 1"
    "_AmbientScaleHDR" "1"
    "_light" "CURRENT_LIGHT"
    "_lightHDR" "-1 -1 -1 1"
    "_lightscaleHDR" "1"
    "angles" "CURRENT_ANGLE"
    "pitch" "0"
    "SunSpreadAngle" "0"
    "origin" "0 0 73"
    editor
    {
        "color" "220 30 220"
        "visgroupshown" "1"
        "visgroupautoshown" "1"
        "logicalpos" "[0 500]"
    }
}
'''
skybox = 'sky_tf2_04'
batchtext = '''
set ftypename=Easy TF2 Mapper Save
set extension=.ezm
set pathtoexe="EasyTF2Mapper.exe"
set pathtoicon="icons/icon.ico"

if %pathtoicon%=="" set pathtoicon=%pathtoexe%,0
REG ADD HKEY_CLASSES_ROOT\%extension%\ /t REG_SZ /d %ftypename% /f
REG ADD HKLM\SOFTWARE\Classes\%ftypename%\DefaultIcon\ /t REG_SZ /d %pathtoicon% /f
ftype %ftypename%=%pathtoexe% "%%1" %%*import pickle
import pprint
import random
import glob
import webbrowser
import wave
import zipfile
import shutil
import winsound

class GridBtn(QWidget):
    def __init__(self, parent, x, y, btn_id):
        super(GridBtn, self).__init__()
        self.button = QPushButton("", parent)
        self.x = x
        self.y = y
        self.btn_id = btn_id
        #self.button.move(self.x,self.y)
        self.button.resize(32,32)
        self.button.setFixedSize(32, 32)

assoc %extension%=%ftypename%
'''
#skyboxlight = '255 255 255 200'
#skyboxangle = '0 0 0'
#if the user does not change the lighting, it sticks with this.
#if the user does not choose a skybox it sticks with this

prefab_file = open("prefab_template/prefab_list.txt")
prefab_text_file = open("prefab_template/prefab_text_list.txt")
prefab_icon_file = open("prefab_template/prefab_icon_list.txt")

skybox_file = open("prefab_template/skybox_list.txt")
skybox_icon = open("prefab_template/skybox_icons.txt")
skybox_light = open("prefab_template/skybox_light.txt")
skybox_angle = open("prefab_template/skybox_angle.txt") 

prefab_list.append([])
section=0
for line in prefab_file.readlines():
    if line == '\n':
        prefab_list.append([])
        section+=1
    else:
        prefab_list[section].append(line[:-1] if line.endswith("\n") else line)# need to do this because reading the file generates a \n after every line
section=0
prefab_text_list.append([])
for line in prefab_text_file.readlines():
    if line == '\n':
        prefab_text_list.append([])
        section+=1
    else:
        prefab_text_list[section].append(line[:-1] if line.endswith("\n") else line)

section=0
prefab_icon_list.append([])
for line in prefab_icon_file.readlines():
    if line == "\n":
        prefab_icon_list.append([])
        section +=1
    else:
        prefab_icon_list[section].append(line[:-1] if line.endswith("\n") else line)

f = open('prefab_template/rot_prefab_list.txt', 'r+')
lns = f.readlines()
f.close()

section = 0
rotation_icon_list = []
index_section_list = [0]
rotation_icon_list.append([])
for index,line in enumerate(lns):
    if line == '\n':
        index_section_list.append(index)
        rotation_icon_list.append([])
        section+=1
    else:
        rotation_icon_list[section].append(line[:-1] if '\n' in line else line)
print(index_section_list)
for line in skybox_file.readlines():
    skybox_list.append(line[:-1] if line.endswith("\n") else line)# need to do this because reading the file generates a \n after every line

for line in skybox_icon.readlines():
    skybox_icon_list.append(line[:-1] if line.endswith("\n") else line)

for line in skybox_light.readlines():
    skybox_light_list.append(line[:-1] if line.endswith("\n") else line)

for line in skybox_angle.readlines():
    skybox_angle_list.append(line[:-1] if line.endswith("\n") else line)
    
for file in [prefab_file, prefab_text_file, prefab_icon_file,skybox_file,skybox_icon,skybox_angle,skybox_light]:
    file.close()

#imports that need prefab_list to be defined
for sec in prefab_list:
    for item in sec:
        if item:
            globals()[item] = importlib.import_module(item)
            print("import", item)
            save_dict[item]=eval(item)
            load_dict[eval(item)]=item

logo = open('logo.log','r+')
logo_f = logo.readlines()
for i in logo_f:
    print(i[:-1])
logo.close()

print("\n~~~~~~~~~~~~~~~~~~~~~\nMapper loaded! You may have to alt-tab to find the input values dialog.\n")


#Main Program
app = QApplication(sys.argv)
gui = MainWindow()




app.exec_()



#to get this working we're going to need a global variable that is the number
#of the currently selected tab. (eg 1, 2, 3) This can be defined when the event
#tab.changed.connect or something along those lines happens
#
#IS ACTUALLY list_tab_widget.currentIndex() (returns int)
#
#at the top of every function that references the old tile_list, write something like
#current_prefab_tab = eval('tile_list%d' % CURRENT_TAB+1)
#and replace all instances of the tile_list with current_prefab_tab
#
#when loading all the prefabs, if the line is blank, add a new sublist. When referencing the
#prefab_list, use prefab_list[CURRENT_TAB][current_prefab_tab.index]
#
#When changing order of the prefabs, change the list, and when user EXITS the program, change the files 
#
#UNKNOWN TODO
#Figure out a way to decide which tab newly created prefabs should be placed in.
#Figure out how to move prefabs from tab to tab
