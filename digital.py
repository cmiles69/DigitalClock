#!/usr/bin/env python3
# coding = utf-8

# Web Code
# https://www.youtube.com/watch?v=pTaZXZ3VYCc
# 3:38, 4:17, 5:24, 5:44, 6:33, 7:21, 8:14, 8:34
# 9:29, 10:41, 12:35, 13:29, 15:55

# Craig Miles -> cmiles69@hushmail.com

import os
import time
import tkinter
from tkinter import font

class DigitalClock( object ):

    def __init__( self, root ):
        self.root = root
        # Change directory to current working file
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        os.chdir( BASE_DIR )
        # print( os.getcwd())
        self.initUI()

    def initUI( self ):
        self.root.title( 'Digital Clock' )
        self.geometry = self.screen_size( size = 0.50 )
        # print( self.geometry )
        self.root.geometry( self.geometry )
        self.center_root()
        self.root.configure( background = '#081923' )
        self.setup_fonts()
        self.create_labels()
        self.clock()

    def screen_size( self, size ):
        # Obtain desired screen size
        width = self.root.winfo_screenwidth() * size
        height = self.root.winfo_screenheight() * size
        return( '{}x{}+{}+{}' 
        .format( int( width ), int( height ), 0, 0 ))

    def center_root( self ):
        self.root.update_idletasks()
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        pos_right = \
        int( self.root.winfo_screenwidth() // 2 - window_width // 2 )
        pos_down = \
        int( self.root.winfo_screenheight() // 2 - window_height // 2 )
        self.root.geometry( '{}x{}+{}+{}'
        .format( window_width, window_height, pos_right, pos_down ))

#============================Setup Fonts================================        

    def setup_fonts( self ):
        self.lbl_font = font.Font( family = 'DejaVu Serif',
                                   size = 50,
                                   weight = 'bold' )
        # self.txt_font = font.Font( family = 'Bitstream Charter',
        #                            size = 25,
        #                            weight = 'normal' )
        # self.txt_font = font.Font( family = 'FreeSerif',
        #                            size = 25,
        #                            weight = 'normal' )
        self.txt_font = font.Font( family = 'Liberation Mono',
                                   size = 25,
                                   weight = 'normal' )

#===========================Create labels===============================

    def create_labels( self ):
        self.lbl_hour = tkinter.Label( root,
                                       font = self.lbl_font,                                                  
                                       text = '12',
                                       background = '#0875B7',
                                       foreground = 'white' )
        self.lbl_hour.place( x = 150,
                             y = 100,
                             width = 150,
                             height = 150 )

        self.txt_hour = tkinter.Label( root,
                                       font = self.txt_font,                                                  
                                       text = 'Hour',
                                       background = '#0875B7',
                                       foreground = 'white' )
        self.txt_hour.place( x = 150,
                             y = 260,
                             width = 150,
                             height = 50 )

        self.lbl_minute = tkinter.Label( root,
                                         font = self.lbl_font,                                                  
                                         text = '12',
                                         background = '#913555',
                                         foreground = 'white' )
        self.lbl_minute.place( x = 320,
                               y = 100,
                               width = 150,
                               height = 150 )

        self.txt_minute = tkinter.Label( root,
                                         font = self.txt_font,                                                  
                                         text = 'Minute',
                                         background = '#913555',
                                         foreground = 'white' )
        self.txt_minute.place( x = 320,
                               y = 260,
                               width = 150,
                               height = 50 )

        self.lbl_seconds = tkinter.Label( root,
                                          font = self.lbl_font,                                                  
                                          text = '12',
                                          background = '#3d6646',
                                          foreground = 'white' )
        self.lbl_seconds.place( x = 490,
                                y = 100,
                                width = 150,
                                height = 150 )

        self.txt_seconds = tkinter.Label( root,
                                         font = self.txt_font,                                                  
                                         text = 'Seconds',
                                         background = '#3d6646',
                                         foreground = 'white' )
        self.txt_seconds.place( x = 490,
                                y = 260,
                                width = 150,
                                height = 50 )

        self.lbl_am = tkinter.Label( root,
                                     font = self.lbl_font,                                                  
                                     text = 'AM',
                                     background = '#6e2626',
                                     foreground = 'white' )
        self.lbl_am.place( x = 660,
                           y = 100,
                           width = 150,
                           height = 150 )

        self.txt_noon = tkinter.Label( root,
                                       font = self.txt_font,                                                  
                                       text = 'Noon',
                                       background = '#6e2626',
                                       foreground = 'white' )
        self.txt_noon.place( x = 660,
                             y = 260,
                             width = 150,
                             height = 50 )

#===========================Clock=======================================

    def clock( self ):
        self.hours   = str( time.strftime( '%-H' ))
        # self.hours = 0
        self.minutes = str( time.strftime( '%M' ))
        self.seconds = str( time.strftime( '%S' ))

        if int( self.hours ) >= 12 and int( self.minutes ) > 0:
            self.lbl_am.configure( text = 'PM' )

        # if int( self.hours ) > 12:
        #     self.hours = str(( int( self.hours ) - 12 ))

        # print( self.hours,
        #        self.minutes,
        #        self.seconds )

        self.lbl_hour.configure( text = self.hours )
        self.lbl_minute.configure( text = self.minutes )
        self.lbl_seconds.configure( text = self.seconds )

        self.lbl_seconds.after( 200, self.clock )

#============================END========================================        

if __name__ == '__main__':
    root = tkinter.Tk()
    application = DigitalClock( root )
    root.mainloop()