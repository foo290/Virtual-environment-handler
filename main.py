from oops3 import *
from os import getcwd
from ctypes import windll
from tfl_backend import (ver, check_python_path, Core_ops,
                         Data_IO, chk_valid_path_for_ve,
                         universal_Path_database,
                         Install_Pakages, validate_script, set_current, Current_default_env,
                         Current_default_env_dir)
from directory_manager import base_Directory, python_paths, emptyFileHandler
import properties
from preLoader import check_installed_Python
import firstTimeExe

firstexecute = firstTimeExe.update_basedir_and_default_ve()
print(firstexecute)

err = windll.shcore.SetProcessDpiAwareness(2)

installed = getcwd()
window_counter = 0
ve_creationWinCounter = 0
pkg_installation_win_counter = 0

width = 930
height = 580
# Primary_execution().get_currently_active()


retCode = check_installed_Python()
if not retCode:
    messagebox.showwarning('File Not Found', 'Python Interpreter not found')


def set_PRIMARY():
    global Current_default_env_dir, Current_default_env
    result = set_current()
    if result[0]:
        Current_default_env = result[1]
        Current_default_env_dir = result[2]
    else:
        pass


set_PRIMARY()


def mainWinTitle(root, title):
    root.title(f'Environment Launcher    |   Active Environment : -{title}')


mainPath = ''

launch_terminator = 0


class Extended_Panels:
    def __init__(self, root=None):
        self.parent = root

        pass

    def Agness(self, heading, content, type=None):
        global launch_terminator
        if not launch_terminator:
            launch_terminator = 1
            width = 1000
            height = 600
            if type:
                root = Tk(self.parent)
            else:
                root = Toplevel(self.parent)

            animate(root)

            x = (root.winfo_screenwidth() // 2) - (width // 2)
            y = (root.winfo_screenheight() // 2) - (height // 2)
            root.geometry(f'{width}x{height}+{x}+{y}')
            root.overrideredirect(1)
            root.attributes('-topmost', 1)

            rootcan = Mainframe2().customcan(root, width, height, 'white', 0, 0)
            img = PhotoImage(file='Configuration/panel01.png')
            rootcan.create_image(0, 0, image=img, anchor=NW)
            rootcan.create_text(520, 20, text=heading, font='"Ebrima" 17 bold', fill='black', anchor=NW)
            rootcan.create_line(520, 70, 980, 70, fill='#bbbbbb', width=2)
            text = content
            rootcan.create_text(520, 100, text=text, font='"Ebrima" 11 ', fill='black', anchor=NW)
            rootcan.create_text(520, height - 50, text='A g n e s s', font='"Rog fonts" 15 ', fill='#acacac', anchor=NW)
            rootcan.create_text(700, height - 45, text='Ai', font='"Ebrima" 11 bold ', fill='#acacac', anchor=NW)

            def safeExit():
                global launch_terminator
                launch_terminator = 0
                animate(root, 'fade')
                root.after(600, lambda: root.destroy())
                # root.quit()
                # root.destroy()

            but = Mainframe2().custombuttons(rootcan, 'Okay!', 20, 1, safeExit, width - 200, height - 50)
            but.config(borderwidth=2, relief='groove', cursor='hand2')
            root.protocol('WM_DELETE_WINDOW', safeExit)
            root.mainloop()


if firstexecute != 'redundant':
    Extended_Panels().Agness(properties.first_heading, properties.first, type='First')


# Extended_Panels().error(intro_headinf,intro)


class Prefrences_Frontend(Mainframe2):
    def __init__(self, frontRoot):
        self.FrontRoot = frontRoot

        self.root_Prefrences = Toplevel()
        self.max_width = self.root_Prefrences.winfo_screenwidth()
        self.max_height = self.root_Prefrences.winfo_screenheight()
        min_width = self.max_width // 2
        min_height = self.max_height // 2
        self.root_Prefrences.config(background=properties.prefrences_root_clr)
        self.root_Prefrences.iconbitmap(self.root_Prefrences, properties.icon_image)

        mainWinTitle(self.root_Prefrences, Current_default_env)

        self.headerCLR = properties.headerCLR

        self.root_Prefrences.state('zoom')
        self.root_Prefrences.minsize(min_width, min_height)
        self.root_Prefrences.maxsize(self.max_width, self.max_height)

        self.root_can = super().customcan(self.root_Prefrences, self.max_width, self.max_height,
                                          properties.prefrences_root_clr, 0, 0)

        """ Root Back Image """
        # self.root_can.create_image(0, 0, image=root_img, anchor=NW)

        """ Header Image """
        header = super().customcan(self.root_can, self.max_width, 70, self.headerCLR, 0, 0)
        header.create_text(self.max_width // 2, 30, text='Environment Launcher', font='"Century gothic" 30', fill='white',
                           anchor=CENTER)
        header.create_line(0, 66, self.max_width, 66, width=3, fill=properties.secondaryClr)

        footer = super().customcan(self.root_can, self.max_width, 70, properties.secondaryClr, 0, self.max_height - 110)

        footer.create_text(self.max_width // 2, 10, text='ver 1.0', font='10', anchor=NW, fill='white')
        footer.create_text(70, 20, text='Nitin Sharma', font='Ebrima 8', anchor=CENTER,
                           fill='white')

        """    Functions Calls   """
        self.left_side_bar()
        self.main_display()
        self.right_bar_icons()

        def safeExit():
            global window_counter
            window_counter = 0
            self.root_Prefrences.quit()
            self.root_Prefrences.destroy()

        self.root_Prefrences.protocol('WM_DELETE_WINDOW', safeExit)
        self.root_Prefrences.mainloop()

    def left_side_bar(self):
        l_side_panel = super().customcan(self.root_can, width // 2, self.max_height - 230, properties.leftbarCLR, 20,
                                         80)
        l_side_panel.create_line(0, self.max_height - 330, width // 2, self.max_height - 330,
                                 fill=properties.secondaryClr, width=2)
        l_side_panel.create_line(0, self.max_height - 235, width // 2, self.max_height - 235,
                                 fill=properties.secondaryClr, width=8)

        heading = l_side_panel.create_text(70, 20, text='Your Environments (VE)', anchor=NW, font='Ebrima 18 bold',
                                           fill='white')
        l_side_panel.create_line(0, 80, width // 2, 80, fill=properties.secondaryClr, width=5)

        """     Create New Environment Function     """

        def create_new_VE(event):
            global ve_creationWinCounter

            if ve_creationWinCounter == 0:
                ve_creationWinCounter = 1
                width = 700
                height = 400
                root = Toplevel()
                x = (root.winfo_screenwidth() // 2) - (width // 2)
                y = (root.winfo_screenheight() // 2) - (height // 2)
                root.geometry(f'{width}x{height}+{x}+{y}')
                root.resizable(0, 0)
                root.focus()
                img = PhotoImage(file=properties.toplevel_1_createNVE_img)
                root_can = Mainframe2().customcan(root, width, height, 'white', 0, 0)
                root_can.create_image(0, 0, image=img, anchor=NW)

                root.title('Create Virtual Environment')

                """ NAME """
                root_can.create_text(20, 50, text='Name : ', anchor=NW, font='Ebrima 12')
                name_variable1 = StringVar()
                name = Entry(root_can, width=50, highlightthickness=2,
                             highlightbackground=properties.components_borderClr_B, textvariable=name_variable1)
                name.place(x=130, y=55)

                """ PATH """

                def get_path():
                    global mainPath
                    raw_path = filedialog.askdirectory(title='Target Directory of VE', parent=root)
                    if raw_path:
                        mainPath = raw_path
                        path_variable2.set(raw_path)

                root_can.create_text(20, 100, text='Path : ', anchor=NW, font='Ebrima 12')
                path_variable2 = StringVar()
                path = Entry(root_can, width=50, highlightthickness=2, highlightbackground='black',
                             textvariable=path_variable2)
                path.place(x=130, y=100)
                path_variable2.set(base_Directory)

                but2 = Mainframe2().custombuttons(root_can, 'Browse', 15, 1, get_path, width - 150, 97)
                but2.config(relief='solid', borderwidth=0, fg='white', bg=properties.primaryClr)

                """ PYTHON VERSION """
                root_can.create_text(20, 150, text='Python : ', anchor=NW, font='Ebrima 12')
                py_ver_variable3 = StringVar()
                py_ver = Entry(root_can, width=50, highlightthickness=2, highlightbackground='black',
                               textvariable=py_ver_variable3)
                py_ver.place(x=130, y=155)

                but3 = Mainframe2().custombuttons(root_can, 'get python', 15, 1, None, width - 150, 152)
                but3.config(relief='solid', borderwidth=0, fg='white', bg=properties.primaryClr)

                """ PYTHON PATHS """

                def getPyVer():
                    global mainPath
                    raw_path = filedialog.askdirectory(title='select path where python.exe exist', parent=root)
                    if raw_path:
                        mainPath = raw_path
                        authenticate = validate_script(raw_path, 'python.exe')
                        if authenticate[0]:
                            path_combobox.set(raw_path)
                            py_ver_variable3.set(authenticate[1])
                            root_can.itemconfig(self.pyver_info,
                                                text=f'Python dir is changed and current ver is {authenticate[1]}')
                        else:
                            Extended_Panels(root).Agness(properties.pythonnotfound_heading, properties.pythonnotfound)

                root_can.create_text(20, 210, text='Python Dir : ', anchor=NW, font='Ebrima 12')

                path_combobox_obj = Mainframe2()
                path_combobox = path_combobox_obj.customcombobox(root_can, '', None, 48, 130, 210)
                but4 = Mainframe2().custombuttons(root_can, 'Browse', 15, 1, getPyVer, width - 150, 207)
                but4.config(relief='solid', borderwidth=0, fg='white', bg='#425066')

                if ver[0]:
                    interpreter_path = list(ver[1].values())
                    ver_name = list(ver[1].keys())

                    if "-3.7-64" in ver_name:
                        ind_ = ver_name.index('-3.7-64')
                        path_combobox.set(ver[1][ver_name[ind_]])
                        py_ver_variable3.set(ver_name[ind_])

                    else:
                        path_combobox.set(ver[1][ver_name[0]])
                        py_ver_variable3.set(ver_name[0])
                    path_combobox.config(values=interpreter_path)

                    py_ver.config(highlightthickness=2, highlightbackground='green', state='readonly')
                    self.pyver_info = root_can.create_text(130, 185,
                                                           text=f'Suitable python version found version : -3.7-64',
                                                           fill='green', anchor=NW)
                    but3.config(state=DISABLED)

                else:
                    py_ver.config(highlightthickness=2, highlightbackground='red')
                    root_can.create_text(130, 185,
                                         text='Supported python version not found.\nInstall any python ',
                                         fill='red', anchor=NW)

                    installed_vers_path = check_python_path()
                    if installed_vers_path != 404:
                        path_combobox.set(installed_vers_path)
                    else:
                        interpreternotfound = f'Oops! Something is not as what i expected.\n\n' \
                                              f'Supported python version not found.\nI have looked in' \
                                              f'following dirs: \n\n{python_paths[0]}\n{python_paths[1]}' \
                                              f'\n{python_paths[2]}\n{python_paths[3]}\n{python_paths[4]}' \
                                              f'\n\nTry giving python path manually or install if its not install.\n\n\n{"    " * 18}-Agness'
                        Extended_Panels(root).Agness(properties.interpreternotfound_heading, interpreternotfound)

                root_can.create_text(20, 260,
                                     text='Do Not Change default settings until you know what u are doing.',
                                     fill='red', anchor=NW)

                def setVerAccPath(event):
                    path_SELECTED = path_combobox_obj.getcombodata()
                    for p in list(ver[1].values()):
                        if p == path_SELECTED:
                            tempIND = list(ver[1].values()).index(p)
                            py_ver_variable3.set(list(ver[1].keys())[tempIND])

                path_combobox.bind('<<ComboboxSelected>>', setVerAccPath)

                """ Main Buttons """
                process_status = root_can.create_text(20, 300, text='', font='"Rog fonts" 13',
                                                      anchor=NW)

                def submit_information():

                    """ Validation Begins here"""
                    VE_name = name_variable1.get().strip()
                    VE_path = path_variable2.get().strip()
                    VE_python = py_ver_variable3.get().strip()
                    VE_python_path = path_combobox_obj.getcombodata().strip()

                    def test():
                        root.destroy()

                    def safeExithread():
                        global ve_creationWinCounter
                        ve_creationWinCounter = 0
                        try:
                            safeExit()
                        except:
                            pass

                    def internalTHREAD():
                        response = Core_ops().create_new_virtual_environment(VE_name, VE_path, VE_python_path)

                        if response == 'success':
                            root_can.itemconfig(process_status, text='Complete !', fill='green')
                            messagebox.showinfo('SUCCESS', 'Virtual Environment is created successfully.', parent=root)
                            # universal_Path_database('write',VE_name,VE_path)
                            self.countVEs()
                            safeExithread()
                        elif response == 'customPythonPathWrong':
                            root_can.itemconfig(process_status, text='Failed !', fill='red')
                            messagebox.showerror('Fatal Error!', 'This path for python interpreter does not exist.',
                                                 parent=root)
                        elif response == 'pythonNotFound':
                            root_can.itemconfig(process_status, text='Failed !', fill='red')
                            messagebox.showerror('Python Interpreter NotFound',
                                                 'Python interpreter not found', parent=root)
                        elif response == -201:
                            root_can.itemconfig(process_status, text='Failed !', fill='red')
                            messagebox.showerror(properties.vealreadyexist_heading,
                                                 'This name is owned by another VE already.', parent=root)
                        elif response == 'pathDontExist':
                            root_can.itemconfig(process_status, text='Failed !', fill='red')
                            messagebox.showerror('Fatal Error!', 'The path for virtual environment does not exist.',
                                                 parent=root)
                        else:
                            root_can.itemconfig(process_status, text='Failed !', fill='red')

                    if (VE_name != '' and VE_path != '' and VE_python != '' and VE_python_path != ''):
                        from threading import Thread
                        t1 = Thread(target=internalTHREAD)
                        t1.daemon = 1
                        t1.start()
                        root_can.itemconfig(process_status, text='Processing . . . .', fill='black')

                    else:
                        messagebox.showerror('Empty Field',
                                             'Every Field is required in order to create VE. Missing info can '
                                             'lead to Fatal Error or Malfunction.', parent=root)

                submit = Mainframe2().custombuttons(root_can, 'Create', 20, 1, submit_information, 50, height - 50)
                submit.config(relief='solid', borderwidth=0, fg='white', bg='green')

                def safeExit():
                    global ve_creationWinCounter
                    ve_creationWinCounter = 0
                    root.destroy()

                root.protocol('WM_DELETE_WINDOW', safeExit)
                root.mainloop()

        but1 = super().customcan(l_side_panel, width // 2, 80, '#ff8c00', 0, self.max_height - 323)
        add_sign = super().customcan(but1, 70, 70, 'white', 5, 5)
        add_sign.create_text(18, 7, text='+', font='none 35', anchor=NW)
        add_sign.config(cursor='hand2')
        but1.config(cursor='hand2')
        but1.create_text(width // 4 + 10, 80 // 2, text='Create New Environment', anchor=CENTER,
                         font='Ebrima 15 bold underline',
                         fill='white')

        but1.bind('<Button-1>', create_new_VE)
        add_sign.bind('<Button-1>', create_new_VE)

        """     Display Current Environments    """
        holder_hight = (self.max_height - 230) - 200
        if holder_hight > 500:
            h_coord = holder_hight // 40
            x_coor = 5
        else:
            h_coord = holder_hight // 30
            x_coor = 35

        self.list_obj = Mainframe2()
        list_box_holder = super().customframes(l_side_panel, width // 2, (self.max_height - 230) - 200, 'white', x_coor,
                                               120)

        self.list_box = self.list_obj.customListBox(list_box_holder, 35, h_coord, LEFT)
        self.list_box.config(selectmode=SINGLE)
        self.list_box.config(font='Ebrima 15', borderwidth=0, bg=properties.maindisplay_CLR,
                             fg=properties.defaultTxtClr, highlightthickness=0,
                             justify=CENTER, activestyle='none', cursor='hand2')
        self.countVEs()

    def countVEs(self):
        ve_list = Core_ops().get_VE()
        self.list_box.delete(0, END)
        if ve_list[0] != -1:
            self.list_obj.listBox_values(ve_list[1])
        else:
            self.list_obj.listBox_values(ve_list[1])
            Extended_Panels(self.root_Prefrences).Agness(properties.coreenvnotfound_heading, properties.coreenvnotfound)

    def main_display(self):

        main_root = super().customcan(self.root_can, self.max_width - 600, self.max_height - 230,
                                      properties.maindisplay_CLR, 500, 80)
        main_root.create_text(20, 20, text='Current Default VE : ', font='Ebrima 20 bold', anchor=NW,
                              fill=properties.defaultTxtClr)

        main_root.create_text(350, 20, text=Current_default_env, font='Ebrima 20', anchor=NW,
                              fill=properties.defaultTxtClr)

        """ Showing Details of selected VE """
        nameKey = main_root.create_text(20, 100, text='Virtual Env Name : ', font='Ebrima 10 bold', anchor=NW,
                                        fill=properties.defaultTxtClr)
        nameValue = main_root.create_text(220, 100, text=Current_default_env, font='Ebrima 10 ', anchor=NW,
                                          fill=properties.defaultTxtClr)

        dirKey = main_root.create_text(20, 140, text='Origin : ', font='Ebrima 10 bold', anchor=NW,
                                       fill=properties.defaultTxtClr)
        dirValue = main_root.create_text(220, 140, text=Current_default_env_dir, font='Ebrima 10 ', anchor=NW,
                                         fill=properties.defaultTxtClr)

        pkgKey = main_root.create_text(20, 240, text='Installed packages : ', font='Ebrima 10 bold', anchor=NW,
                                       fill=properties.defaultTxtClr)

        mainroot_HEIGHT = self.max_height - 230
        if mainroot_HEIGHT > 700:
            h_coor = 18
        else:
            h_coor = 11

        pkgList_holder = Mainframe2().customframes(main_root, 400, 300, properties.maindisplay_CLR, 20, 280)
        self.pkgListBox_obj = Mainframe2()
        pkgListBox = self.pkgListBox_obj.customListBox(pkgList_holder, 35, h_coor, LEFT)
        pkgListBox.config(font='Ebrima 11', borderwidth=0, bg=properties.maindisplay_CLR, fg=properties.defaultTxtClr,
                          highlightthickness=0,
                          activestyle='none')

        if Current_default_env_dir != base_Directory:
            try:
                pkgtup = Core_ops().get_Packages(Current_default_env, Current_default_env_dir, 'external')
                pkgs, _ = pkgtup
                self.pkgListBox_obj.listBox_values(pkgs)
            except:
                pass
        else:
            try:
                pkgtup = Core_ops().get_Packages(Current_default_env, Current_default_env_dir, 'internal')
                pkgs, _ = pkgtup
                self.pkgListBox_obj.listBox_values(pkgs)
            except:
                pass

        """ Buttons """

        def activateVENV():

            if self.list_obj.get_List_selected() != -1:
                selected_VE = self.list_obj.get_List_selected()[0]

                if Current_default_env == selected_VE:
                    Extended_Panels(self.root_Prefrences).Agness(properties.alreadyactive_heading,
                                                                 properties.alreadyactive)
                else:
                    resp = messagebox.askokcancel('Activate Virtual Environment',
                                                  f'Selected VE : {selected_VE} will be activated and set as default.',
                                                  parent=self.root_Prefrences)
                    if resp:
                        """ Checking for validity of VE python """
                        absPath = universal_Path_database('read', selected_VE, '')
                        retCode = chk_valid_path_for_ve(f'{absPath}', name=selected_VE)

                        if retCode:
                            Data_IO().writeDefaultVE(selected_VE)
                            set_PRIMARY()

                            activateenv = f'The selected environment is activated successfully\nand is online now.\n\n' \
                                          f'Activated Env : {selected_VE}\n\nStatus : Online\n\n\n{"    " * 18}-Agness'
                            Extended_Panels(self.root_Prefrences).Agness('Online...', activateenv)
                            self.main_display()
                            mainWinTitle(self.root_Prefrences, Current_default_env)
                            mainWinTitle(self.FrontRoot, Current_default_env)
                        else:
                            messagebox.showerror('Invalid VE',
                                                 'The main python script not found in the selected VE. The directory is corrupted.',
                                                 parent=self.root_Prefrences)

        def deleteVE():

            if self.list_obj.get_List_selected() != -1:
                selected_VE = self.list_obj.get_List_selected()[0]
                if selected_VE == emptyFileHandler:
                    Extended_Panels(self.root_Prefrences).Agness(properties.accessdeniedvedel_heading,
                                                                 properties.accessdeniedvedel)
                else:
                    resp = messagebox.askyesno('Delete Confirmation',
                                               f'Do you want to delete selected Environment : {selected_VE} ?',
                                               parent=self.root_Prefrences)
                    if resp:
                        delete_status = Core_ops().deleteVENV(selected_VE)
                        if delete_status:
                            if selected_VE == Current_default_env:
                                Data_IO().writeDefaultVE(emptyFileHandler)
                                set_PRIMARY()
                                mainWinTitle(self.FrontRoot, Current_default_env)
                                mainWinTitle(self.root_Prefrences, Current_default_env)
                            self.countVEs()
                            universal_Path_database('delete', selected_VE, 'none')

                            mgs = f'The operation was a success... Woohoo!!!' \
                                  f'\n\nThe selected VE is deleted from my database.\n\nTarget : {selected_VE}    |    Status : Success\n\n\n{"    " * 18}-Agness'
                            Extended_Panels(self.root_Prefrences).Agness(properties.vedeleted_heading, mgs)
                            self.main_display()
                            self.countVEs()
                        else:
                            messagebox.showerror('Rare Case',
                                                 f'Something is not as what we expected. An Error encountered while deleteing.',
                                                 parent=self.root_Prefrences)

        main_root.create_line(0, self.max_height - 330, self.max_width - 600, self.max_height - 330, fill='#425066',
                              width=2)
        main_root.create_line(0, self.max_height - 235, self.max_width - 600, self.max_height - 235, fill='#ff8c00',
                              width=10)

        but1 = Mainframe2().custombuttons(main_root, 'Activate', 15, 1, activateVENV, self.max_width - 800,
                                          self.max_height - 300)
        but1.config(relief='solid', fg='white', bg='green', borderwidth=0, font='Ebrima 11')

        but1 = Mainframe2().custombuttons(main_root, 'Delete', 15, 1, deleteVE, self.max_width - 980,
                                          self.max_height - 300)
        but1.config(relief='solid', fg='white', bg='#ff8c00', borderwidth=0, font='Ebrima 11')

        def show_selected(name, path, caller):
            if path:
                pkgListBox.delete(0, END)
                main_root.itemconfig(nameKey, text='Virtual Env Name : ', fill=properties.defaultTxtClr)
                main_root.itemconfig(nameValue, text=name, fill=properties.defaultTxtClr)

                main_root.itemconfig(dirKey, text='Origin : ', fill=properties.defaultTxtClr)
                main_root.itemconfig(dirValue, text=path, fill=properties.defaultTxtClr)

                if path != base_Directory:
                    self.temp_dir_info = main_root.create_text(self.max_width - 1000, 140,
                                                               text=f'This Virtual Environment is from another Directory',
                                                               anchor=NW, fill='red')
                    main_root.itemconfig(dirValue, fill='red')
                else:
                    main_root.itemconfig(dirValue, fill=properties.defaultTxtClr)
                    try:
                        main_root.delete(self.temp_dir_info)
                    except:
                        pass

                returnCode = Core_ops().get_Packages(name[0], path, caller)

                if returnCode != -1:
                    pkgs1, modules1 = returnCode
                    self.pkgListBox_obj.listBox_values(pkgs1)
                else:
                    pass
            else:
                messagebox.showerror('Invalid Env', 'No valid Entry found in database for selected VE',
                                     parent=self.root_Prefrences)

        def get_selected(event):
            selected = self.list_obj.get_List_selected()

            if selected != -1:
                path = universal_Path_database('read', selected[0], 'none')
                if path == base_Directory:
                    show_selected(selected, base_Directory, 'internal')

                else:
                    show_selected(selected, path, 'external')

        self.list_box.bind('<ButtonRelease-1>', get_selected)

        main_root.create_line(0, 80, 650, 80, width=5, fill='#ff8c00')
        main_root.create_line(650, 80, self.max_width - 600, 80, width=5, fill='#425066')

    def right_bar_icons(self):
        open_VEs = super().customcan(self.root_can, 60, 60, properties.maindisplay_CLR, self.max_width - 80, 170)
        open_VEs.config(highlightthickness=1, highlightbackground='white')
        self.root_can.create_text(self.max_width - 50, 250, text='Open VE', anchor=CENTER, fill='white')
        open_VEs.create_text(30, 35, text='', anchor=CENTER, font='none 20 bold', fill='white')

        install_pkg = super().customcan(self.root_can, 60, 60, properties.maindisplay_CLR, self.max_width - 80, 290)
        install_pkg.config(highlightthickness=1, highlightbackground='white')
        self.root_can.create_text(self.max_width - 50, 370, text='pip Install', anchor=CENTER, fill='white')
        install_pkg.create_text(30, 35, text='', anchor=CENTER, font='none 20 bold', fill='white')

        meetagness = super().customcan(self.root_can, 60, 60, properties.maindisplay_CLR, self.max_width - 80, 420)
        meetagness.config(highlightthickness=1, highlightbackground='white')
        self.root_can.create_text(self.max_width - 50, 500, text='Meet Agness', anchor=CENTER, fill='white')
        meetagness.create_text(30, 35, text='', anchor=CENTER, font='none 20 bold', fill='white')

        def Open_VEs_from_dir(event):
            raw_path = filedialog.askdirectory(title='Select Virtual Env', parent=self.root_Prefrences)
            if raw_path:
                veName = raw_path.split('/')[-1]
                if chk_valid_path_for_ve(raw_path):
                    status = universal_Path_database('add', veName, raw_path)
                    if status:
                        self.main_display()
                        self.countVEs()
                    else:
                        Extended_Panels(self.root_Prefrences).Agness(properties.vealreadyexist_heading,
                                                                     properties.vealreadyexist)
                else:
                    Extended_Panels(self.root_Prefrences).Agness(properties.notaVE_heading, properties.notaVE)

        def install_pkgs(event):
            global pkg_installation_win_counter
            selected_env = self.list_obj.get_List_selected()
            if selected_env != -1:
                install_dir_target = universal_Path_database('read', selected_env[0], '')
                if not pkg_installation_win_counter:
                    pkg_installation_win_counter = 1
                    width = 700
                    height = 400
                    pkgroot = Toplevel()
                    x = (pkgroot.winfo_screenwidth() // 2) - (width // 2)
                    y = (pkgroot.winfo_screenheight() // 2) - (height // 2)
                    pkgroot.resizable(0, 0)
                    pkgroot.focus()
                    pkgroot.title('Install Packages -pip install')
                    pkgroot.geometry(f'{width}x{height}+{x}+{y}')

                    img_ = PhotoImage(file='Configuration/pip.png')
                    root_can = Mainframe2().customcan(pkgroot, width, height, 'white', 0, 0)
                    root_can.create_image(0, 0, image=img_, anchor=NW)

                    root_can.create_text(20, 80, text='Pkg Name : ', anchor=NW, font='Ebrima 12', fill='white')
                    pkg_name_variable1 = StringVar()
                    name = Entry(root_can, width=50, highlightthickness=2, highlightbackground='black',
                                 textvariable=pkg_name_variable1)
                    name.place(x=150, y=85)

                    root_can.create_text(20, 130, text='Selected VE : ', anchor=NW, font='Ebrima 12', fill='white')
                    root_can.create_text(150, 135, text=selected_env[0], anchor=NW, fill='white')

                    pkg_path_variable = StringVar()
                    root_can.create_text(20, 175, text='Pkg Path : ', anchor=NW, font='Ebrima 12', fill='white')
                    pkgpath_en = Entry(root_can, width=50, highlightthickness=2, highlightbackground='black',
                                       textvariable=pkg_path_variable)
                    pkgpath_en.place(x=150, y=175)
                    pkg_path_variable.set(f'{install_dir_target}/{selected_env[0]}/Lib/site-packages')

                    def execute_pip():
                        pkg_name = pkg_name_variable1.get()
                        if pkg_name != '':

                            cmd = Install_Pakages().install_pkgs_via_pip(selected_env[0], install_dir_target, pkg_name)
                        else:
                            Extended_Panels(self.root_Prefrences).Agness(properties.pkgname_heading, properties.pkgname)

                    submit = Mainframe2().custombuttons(root_can, 'Install', 20, 1, execute_pip, 50, height - 50)
                    submit.config(relief='solid', borderwidth=0, fg='white', bg='green')

                    def safe_exit():
                        global pkg_installation_win_counter
                        pkg_installation_win_counter = 0
                        pkgroot.quit()
                        pkgroot.destroy()

                    pkgroot.protocol('WM_DELETE_WINDOW', safe_exit)
                    pkgroot.mainloop()

            else:
                Extended_Panels(self.root_Prefrences).Agness(properties.installdirSel_heading, properties.installdirSel)

        open_VEs.bind('<Button-1>', Open_VEs_from_dir)
        install_pkg.bind('<Button-1>', install_pkgs)
        meetagness.bind('<Button-1>',
                        lambda event: Extended_Panels(self.root_Prefrences).Agness(properties.intro_headinf,
                                                                                   properties.intro))


class Front_end(Mainframe2):

    def __init__(self, root):

        self.root = root
        # self.root.overrideredirect(1)
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        mainWinTitle(self.root, Current_default_env)

        self.root.geometry(f'{width}x{height}+{x}+{y}')
        self.root_can = super().customcan(self.root, width, height, 'black', 0, 0)
        # self.root_can.create_text(width//2, height//2-100, text='Environment Launcher', font='Ebrima 18', fill='white')
        # self.root_can.create_text(width // 2, height // 2, text='Underdevelopment', font='Ebrima 18',
        #                           fill='white')

        img = PhotoImage(file=f'{installed}\\{properties.main_frontend_image}')
        self.root_can.create_image(0, 0, image=img, anchor=NW)

        self.root.iconbitmap(self.root, properties.icon_image)

        self.main_panel()
        self.launch_prefrences()
        self.root.resizable(0, 0)
        self.root.focus()

        self.root.mainloop()

    def main_panel(self):

        def safe_exit():
            self.root.quit()
            self.root.destroy()

        #
        # close.bind('<Button-1>', lambda event: safe_exit())

        def open_lab():
            returnCode = Core_ops().open_jupyter(safe_exit, 'jupyter lab')
            if returnCode == 0:
                messagebox.showerror('Fatal Error',
                                     'All VEs are currently offline. Activate a VE from prefrences and try again',
                                     parent=self.root)

        def open_notebook():
            returnCode = Core_ops().open_jupyter(safe_exit, 'jupyter notebook')
            if returnCode == 0:
                messagebox.showerror('Fatal Error',
                                     'All VEs are currently offline. Activate a VE from preferences and try again',
                                     parent=self.root)

        lab = super().custombuttons(self.root_can, 'Jupyter Lab', 20, 1, open_lab, 20, height - 80)
        lab.config(borderwidth=0, relief='solid', font='Ebrima 12 bold', bg='#ff8c00', fg='white', cursor='hand2')

        notebook = super().custombuttons(self.root_can, 'Jupyter Notebook', 20, 1, open_notebook, 300, height - 80)
        notebook.config(borderwidth=0, relief='solid', font='Ebrima 12 bold', bg='#252f48', fg='white', cursor='hand2')

        self.root_can.create_line(0, height - 3, width, height - 3, fill='#ff8c00', width=5)
        self.root_can.create_text(width - 90, height - 20, text='ver  1.0      Nitin Sharma', fill='white',
                                  font='none 7')

    def launch_prefrences(self):
        prefrences_tab = super().customcan(self.root_can, 50, 40, 'black', width - 90, height - 90)
        prefrences_tab.config(cursor='hand2')
        p_icon = prefrences_tab.create_text(8, 0, text='', anchor=NW, font='Ebrima 20 bold', fill='white')
        self.root_can.create_text(width - 95, height - 50, text='Preferences', font='Ebrima 8', anchor=NW,
                                  fill=properties.defaultTxtClr)

        def hover_in(event):
            prefrences_tab.itemconfig(p_icon, fill='#ff8c00')

        def hover_out(event):
            prefrences_tab.itemconfig(p_icon, fill='white')

        prefrences_tab.bind('<Enter>', hover_in)
        prefrences_tab.bind('<Leave>', hover_out)

        def launch_win(event):
            global window_counter
            if window_counter == 0:
                window_counter = 1
                obj = Prefrences_Frontend(self.root)

        prefrences_tab.bind('<Button-1>', launch_win)


Front_end(Tk())
