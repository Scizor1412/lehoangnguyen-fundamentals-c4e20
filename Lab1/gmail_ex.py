from gmail import *
from random import *
sickness = [
    "người yêu em bảo hôm nay ở nhà một mình"
]
gmail = GMail('nguyenlehoang212@gmail.com', 'icepower1995')
html_content = """
<p style="text-align: center;">Cộng h&ograve;a X&atilde; hội Chủ nghĩa Việt Nam</p>
<p style="text-align: center;">Độc lập - Tự do - Hạnh ph&uacute;c</p>
<h1 style="text-align: center;">Đơn xin nghỉ học</h1>
<p>Em ch&agrave;o thầy, em t&ecirc;n l&agrave; L&ecirc; Ho&agrave;ng Nguy&ecirc;n</p>
<p>H&ocirc;m nay em viết đơn n&agrave;y để xin nghỉ học vì {{sickness}}.</p>
<p>Mong thầy th&ocirc;ng cảm.</p>
<p>Em xin cảm ơn</p>
"""

# " mới chia tay người y&ecirc;u n&ecirc;n kh&ocirc;ng thể tập trung cho việc học được&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" />"

msg = Message ('Test Message', to = '20130075@student.hust.edu.vn', html = html_content.replace("{{sickness}}", choice(sickness)))
gmail.send(msg)