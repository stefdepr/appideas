from tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.label = Label(master, text="This is our first GUI!", height=4)
        self.label.pack()

        self.frame_7_8_9_delen = Frame(master)
        self.frame_7_8_9_delen.pack(side=TOP,)

        self.seven_button = Button(self.frame_7_8_9_delen, text="7", width=9, height=4, command=self.greet)
        self.seven_button.pack(in_=self.frame_7_8_9_delen, side=LEFT)
        self.eight_button = Button(self.frame_7_8_9_delen, text="8", width=9, height=4, command=self.greet)
        self.eight_button.pack(in_=self.frame_7_8_9_delen, side=LEFT)
        self.nine_button = Button(self.frame_7_8_9_delen, text="9", width=9, height=4, command=self.greet)
        self.nine_button.pack(in_=self.frame_7_8_9_delen, side=LEFT)
        self.delen_button = Button(self.frame_7_8_9_delen, text="/", width=9, height=4, command=self.greet)
        self.delen_button.pack(in_=self.frame_7_8_9_delen, side=LEFT)

        self.frame_4_5_6_maal = Frame(master)
        self.frame_4_5_6_maal.pack(side=TOP,)
        self.four_button = Button(self.frame_4_5_6_maal, text="4", width=9, height=4, command=self.greet)
        self.four_button.pack(in_=self.frame_4_5_6_maal, side=LEFT)
        self.five_button = Button(self.frame_4_5_6_maal, text="5", width=9, height=4, command=self.greet)
        self.five_button.pack(in_=self.frame_4_5_6_maal, side=LEFT)
        self.six_button = Button(self.frame_4_5_6_maal, text="6", width=9, height=4, command=self.greet)
        self.six_button.pack(in_=self.frame_4_5_6_maal, side=LEFT)
        self.maal_button = Button(self.frame_4_5_6_maal, text="*", width=9, height=4, command=self.greet)
        self.maal_button.pack(in_=self.frame_4_5_6_maal, side=LEFT)

        self.frame_1_2_3_min = Frame(master)
        self.frame_1_2_3_min.pack(side=TOP, )
        self.one_button = Button(self.frame_1_2_3_min, text="1", width=9, height=4, command=self.greet("1"))
        self.one_button.pack(in_=self.frame_1_2_3_min, side=LEFT)
        self.two_button = Button(self.frame_1_2_3_min, text="2", width=9, height=4, command=self.greet)
        self.two_button.pack(in_=self.frame_1_2_3_min, side=LEFT)
        self.three_button = Button(self.frame_1_2_3_min, text="3", width=9, height=4, command=self.greet)
        self.three_button.pack(in_=self.frame_1_2_3_min, side=LEFT)
        self.min_button = Button(self.frame_1_2_3_min, text="-", width=9, height=4, command=self.greet)
        self.min_button.pack(in_=self.frame_1_2_3_min, side=LEFT)

        self.frame_0_comma_is_plus = Frame(master)
        self.frame_0_comma_is_plus.pack(side=TOP, )
        self.zero_button = Button(self.frame_0_comma_is_plus, text="0", width=9, height=4, command=self.greet)
        self.zero_button.pack(in_=self.frame_0_comma_is_plus, side=LEFT)
        self.comma_button = Button(self.frame_0_comma_is_plus, text=",", width=9, height=4, command=self.greet)
        self.comma_button.pack(in_=self.frame_0_comma_is_plus, side=LEFT)
        self.is_button = Button(self.frame_0_comma_is_plus, text="=", width=9, height=4, command=self.greet)
        self.is_button.pack(in_=self.frame_0_comma_is_plus, side=LEFT)
        self.plus_button = Button(self.frame_0_comma_is_plus, text="+", width=9, height=4, command=self.greet)
        self.plus_button.pack(in_=self.frame_0_comma_is_plus, side=LEFT)

        self.frame_reset = Frame(master)
        self.frame_reset.pack(side=TOP, )
        self.reset_button = Button(self.frame_reset, text="reset", width=9, height=4, command=self.greet)
        self.reset_button.pack(in_=self.frame_reset,)



        #self.close_button = Button(self.frame_numbers2, text="Close", command=master.quit)
        #self.close_button.pack(side=BOTTOM)

    def greet(self, text):
        print(text)


root = Tk()
my_gui = MyFirstGUI(root)
root.minsize(280,400)
root.maxsize(280,400)
root.mainloop()