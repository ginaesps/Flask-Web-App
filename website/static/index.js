function deleteNote(noteId) { 
    fetch('/delete-note', { 
        method: 'Post',
        body: JSON.stringify( { noteId: noteId })
    }).then((_res) => {
        window.location.href = "/";
    })
}