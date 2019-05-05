
$(document).on('ready', function () {
    $(function() {
          $('textarea').each(function() {
            var textarea = $(this);
            var mode = textarea.data('editor');
            var editDiv = $('<div>', {
              position: 'absolute',
              width: '100%',
              height: textarea.height(),
              'class': textarea.attr('class')
            }).insertBefore(textarea);
            textarea.css('display', 'none');
            var editor = ace.edit(editDiv[0]);
            editor.renderer.setShowGutter(textarea.data('gutter'));
            editor.getSession().setValue(textarea.val());
            editor.getSession().setMode("ace/mode/" + mode);
            editor.setTheme("ace/theme/idle_fingers");
            editor.setAutoScrollEditorIntoView(true);
            editor.setOption("maxLines", 25);
            editor.setOption("minLines", 5);

            // copy back to textarea on form submit...
            textarea.closest('form').submit(function() {
              textarea.val(editor.getSession().getValue());
            });
            // Prevent editing first and last line of editor
            // editor.commands.on("exec", function(e) {
            //   var rowCol = editor.selection.getCursor();
            //   if ((rowCol.row == 0) || ((rowCol.row + 1) == editor.session.getLength())) {
            //     e.preventDefault();
            //     e.stopPropagation();
            //   }
            // });

          });
        });




});