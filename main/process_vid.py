from services.video_clipper.video_editor import edit_video

from services.video_clipper.video_cutter import cut_video

from services.proccesors.video_handler import process_video

from services.proccesors.edited_video_handler import process_video as edit_handle

from helpers.typewritter import typewriter

print('editing the vid...')
process_video(edit_video)
print('cutting it into pieces..')
edit_handle(cut_video)
print('complete!!!')
typewriter('READY TO SERVE..',0.3,voice=False)
