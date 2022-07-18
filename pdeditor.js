const{spawn}=require('child_process');

const python=spawn('python',['C:\\Users\\User\\PycharmProjects\\pdfeditor\\pdfeditor.py','C:\\Users\\User\\PycharmProjects\\pdfeditor\\ilovepdf_merged.pdf','C:\\Users\\User\\PycharmProjects\\pdfeditor\\Header.jpg']);
python.stdout.on('data',function(data){
  dataToSend=data.toString();
});
python.stderr.on('data', (data) => {
  console.log(data.toString());
});