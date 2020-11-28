document.addEventListener("DOMContentLoaded", function (event) {
    console.log("This is Divyesh");
    let sc=document.createElement('script')
    sc.setAttribute('src', 'https://cdn.tiny.cloud/1/jwd4eruiktd917w3cx8av8sv7x9x4fj35vb3al8chl6syj43/tinymce/5/tinymce.min.js');
    document.head.appendChild(sc);
    sc.onload = ()=>{
        tinymce.init({
        selector: 'textarea',
        plugins: 'autolink autosave lists media table link image',
        toolbar: 'undo redo | styleselect | bold italic underline lineheight strikethrough superscript subscript | alignleft aligncenter alignright alignjustify | bullist numlist | link image  media | outdent indent | forecolor backcolor | table',
        toolbar_mode: 'floating',
        tinycomments_mode: 'embedded',
        tinycomments_author: 'Author name'
      });
    }
    
});