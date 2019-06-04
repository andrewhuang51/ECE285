"""
tools developed for UCSD ECE285 MLIP Project C.

Copyright 2019. Freedom Fighter
"""
import numpy as np

def load_data(root_dir, mode = 'train'):
    '''
    Load from Json files in the same folder
    return dict
    Usage:dd
    train_dic = load_data(root_dir, mode = 'train')
    val_dic = load_data(root_dir, mode = 'val')
    '''
    js_fname = 'pascal_%s2012.json'%mode
    js_dir = Path().absolute()/js_fname
    js_dic = json.load(js_dir.open())
    return js_dic

def hw_bb(bb): return np.array([bb[1], bb[0], bb[3]+bb[1]-1, bb[2]+bb[0]-1])
#convert height/width to bounding box left/right 
def bb_hw(a): return np.array([a[1],a[0],a[3]-a[1]+1,a[2]-a[0]+1])

def show_img(im, figsize=None, ax=None):
    if not ax: fig,ax = plt.subplots(figsize=figsize)
    ax.imshow(im)
    ax.axis('off')
    return ax

def draw_rect(ax, b):
    patch = ax.add_patch(patches.Rectangle(b[:2], *b[-2:], fill=False, edgecolor='white', lw=2))
    draw_outline(patch, 4)

def draw_outline(o, lw):
    o.set_path_effects([patheffects.Stroke(
        linewidth=lw, foreground='black'), patheffects.Normal()])

def draw_text(ax, xy, txt, sz=14):
    text = ax.text(*xy, txt,
        verticalalignment='top', color='white', fontsize=sz, weight='bold')
    draw_outline(text, 1)

# Image with annotation 
def draw_image(im, anno,figsize=(8,6)):
    ax = show_img(im, figsize)
    # draw bbox/class
    for b,c in anno:
#         b = bb_hw(b)
        draw_rect(ax, b) # bounding box
        draw_text(ax, b[:2], cats[c], sz=16)
