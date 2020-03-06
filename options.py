# ###############################################################################
# #  Description: Options page for the game & the possible keys used in the game
# #  Author: Abdullah Najjar
# #  Date: 6 March, 2020
# #  Version: 0.1
# ###############################################################################
import pygame as pg

class options(object):

    # Control options
    Controls = {'ENTER':        pg.K_RETURN,
                'QUIT':         pg.K_ESCAPE,
                'PAUSE':        pg.K_p,
                'MUSIC_TOGGLE': pg.K_m,
                'UP':           pg.K_UP,
                'DOWN':         pg.K_DOWN,
                'LEFT':         pg.K_LEFT,
                'RIGHT':        pg.K_RIGHT,
                'PICKUP':       pg.K_SPACE,
                'SUBMENU_TOGGLE':pg.K_LCTRL,
                }

    # Sound options
    Sound = {'MUSIC_ON':  True,
             'SFX_ON':    True,
             'MUSIC_VOL': 1.0,
             'SFX_VOL':   0.5,
             }

    # Video options
    Video = {'FULLSCREEN': True,
             'RESOLUTION': (800,600),
             }

    #???
    def __init__(self, filename):
        self.filename = filename

    #Set the game to full screen -> move from the source_code file
    def setFullscreen(self, value):
        if self.VIDEO['FULLSCREEN'] and not value:
            pg.display.set_mode(self.VIDEO['RESOLUTION'])
        elif not self.VIDEO['FULLSCREEN'] and value:
            pg.display.set_mode(self.VIDEO['RESOLUTION'], pg.FULLSCREEN)
        self.VIDEO['FULLSCREEN'] = value

    #set the music on
    def setMusicOn(self, value):
        if self.SOUND['MUSIC_ON'] and not value:
            pg.mixer.music.pause()
        elif not self.SOUND['MUSIC_ON'] and value:
            pg.mixer.music.unpause()
        self.SOUND['MUSIC_ON'] = value


    #All keys avaliable I believe
    KEY_TABLE = {
        'BACKSPACE': pg.K_BACKSPACE,
        'TAB': pg.K_TAB,
        'CLEAR': pg.K_CLEAR,
        'RETURN': pg.K_RETURN,
        'PAUSE': pg.K_PAUSE,
        'ESCAPE': pg.K_ESCAPE,
        'SPACE': pg.K_SPACE,
        'EXCLAIM': pg.K_EXCLAIM,
        'QUOTEDBL': pg.K_QUOTEDBL,
        'HASH': pg.K_HASH,
        'DOLLAR': pg.K_DOLLAR,
        'AMPERSAND': pg.K_AMPERSAND,
        'QUOTE': pg.K_QUOTE,
        'LEFTPAREN': pg.K_LEFTPAREN,
        'RIGHTPAREN': pg.K_RIGHTPAREN,
        'ASTERISK': pg.K_ASTERISK,
        'PLUS': pg.K_PLUS,
        'COMMA': pg.K_COMMA,
        'MINUS': pg.K_MINUS,
        'PERIOD': pg.K_PERIOD,
        'SLASH': pg.K_SLASH,
        '0': pg.K_0,
        '1': pg.K_1,
        '2': pg.K_2,
        '3': pg.K_3,
        '4': pg.K_4,
        '5': pg.K_5,
        '6': pg.K_6,
        '7': pg.K_7,
        '8': pg.K_8,
        '9': pg.K_9,
        'COLON': pg.K_COLON,
        'SEMICOLON': pg.K_SEMICOLON,
        'LESS': pg.K_LESS,
        'EQUALS': pg.K_EQUALS,
        'GREATER': pg.K_GREATER,
        'QUESTION': pg.K_QUESTION,
        'AT': pg.K_AT,
        'LEFTBRACKET': pg.K_LEFTBRACKET,
        'BACKSLASH': pg.K_BACKSLASH,
        'RIGHTBRACKET': pg.K_RIGHTBRACKET,
        'CARET': pg.K_CARET,
        'UNDERSCORE': pg.K_UNDERSCORE,
        'BACKQUOTE': pg.K_BACKQUOTE,
        'a': pg.K_a,
        'b': pg.K_b,
        'c': pg.K_c,
        'd': pg.K_d,
        'e': pg.K_e,
        'f': pg.K_f,
        'g': pg.K_g,
        'h': pg.K_h,
        'i': pg.K_i,
        'j': pg.K_j,
        'k': pg.K_k,
        'l': pg.K_l,
        'm': pg.K_m,
        'n': pg.K_n,
        'o': pg.K_o,
        'p': pg.K_p,
        'q': pg.K_q,
        'r': pg.K_r,
        's': pg.K_s,
        't': pg.K_t,
        'u': pg.K_u,
        'v': pg.K_v,
        'w': pg.K_w,
        'x': pg.K_x,
        'y': pg.K_y,
        'z': pg.K_z,
        'DELETE': pg.K_DELETE,
        'KP0': pg.K_KP0,
        'KP1': pg.K_KP1,
        'KP2': pg.K_KP2,
        'KP3': pg.K_KP3,
        'KP4': pg.K_KP4,
        'KP5': pg.K_KP5,
        'KP6': pg.K_KP6,
        'KP7': pg.K_KP7,
        'KP8': pg.K_KP8,
        'KP9': pg.K_KP9,
        'KP_PERIOD': pg.K_KP_PERIOD,
        'KP_DIVIDE': pg.K_KP_DIVIDE,
        'KP_MULTIPLY': pg.K_KP_MULTIPLY,
        'KP_MINUS': pg.K_KP_MINUS,
        'KP_PLUS': pg.K_KP_PLUS,
        'KP_ENTER': pg.K_KP_ENTER,
        'KP_EQUALS': pg.K_KP_EQUALS,
        'UP': pg.K_UP,
        'DOWN': pg.K_DOWN,
        'RIGHT': pg.K_RIGHT,
        'LEFT': pg.K_LEFT,
        'INSERT': pg.K_INSERT,
        'HOME': pg.K_HOME,
        'END': pg.K_END,
        'PAGEUP': pg.K_PAGEUP,
        'PAGEDOWN': pg.K_PAGEDOWN,
        'F1': pg.K_F1,
        'F2': pg.K_F2,
        'F3': pg.K_F3,
        'F4': pg.K_F4,
        'F5': pg.K_F5,
        'F6': pg.K_F6,
        'F7': pg.K_F7,
        'F8': pg.K_F8,
        'F9': pg.K_F9,
        'F10': pg.K_F10,
        'F11': pg.K_F11,
        'F12': pg.K_F12,
        'F13': pg.K_F13,
        'F14': pg.K_F14,
        'F15': pg.K_F15,
        'NUMLOCK': pg.K_NUMLOCK,
        'CAPSLOCK': pg.K_CAPSLOCK,
        'SCROLLOCK': pg.K_SCROLLOCK,
        'RSHIFT': pg.K_RSHIFT,
        'LSHIFT': pg.K_LSHIFT,
        'RCTRL': pg.K_RCTRL,
        'LCTRL': pg.K_LCTRL,
        'RALT': pg.K_RALT,
        'LALT': pg.K_LALT,
        'RMETA': pg.K_RMETA,
        'LMETA': pg.K_LMETA,
        'LSUPER': pg.K_LSUPER,
        'RSUPER': pg.K_RSUPER,
        'MODE': pg.K_MODE,
        'HELP': pg.K_HELP,
        'PRINT': pg.K_PRINT,
        'SYSREQ': pg.K_SYSREQ,
        'BREAK': pg.K_BREAK,
        'MENU': pg.K_MENU,
        'POWER': pg.K_POWER,
        'EURO': pg.K_EURO,
        }
