$(document).ready(function () {
    $('#show-data').click(function() {
        var endpoint = '/answers/' + qid;
        $.ajax({
            url: endpoint,
            error: function() {
                $('#info').html('oops');
            },
            success: function(data) {
                $yes = $('<p>').text("People who answered yes: " + data.yesses);
                $no = $('<p>').text("People who answered no: " + data.nos);
                $('#show-data').append($yes).append($no);
            }
        });
    });
});