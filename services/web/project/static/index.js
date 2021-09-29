/* Formatting function for row details */
function format ( d ) {
    // `d` is the original data object for the row
    return '<table cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;">'+
        '<tr>'+
            '<td>Versions:</td>'+
            '<td>'+d.versions+'</td>'+
        '</tr>'+
        '<tr>'+
            '<td>Module Names:</td>'+
            '<td>'+d.modulenames+'</td>'+
        '</tr>'+
    '</table>';
}

$(document).ready(function() {
    $('#myTable').DataTable({
        "ajax": {
            "url": "http://127.0.0.1:5000/api",
            "dataSrc": "data"
         },
        "deferRender": true,
        //"scrollX": true,
        "responsive": true,
        "order": [[1, "asc"]],
        "language":{
            "paginate": {
                "next": "Next",
                "previous": "Previous"
            }
        },
        "columns":[
            {
                "className": 'details-control',
                "orderable":  false,
                "data":  null,
                "defaultContent": ''
            },
            {"data": "name"},
            {"data": "description"},
            {"data": "category"},
            {"data": "keywords"},
            {"data": "url"}
        ],
        "columnDefs": [
            {
                "targets": 5,
                "data": "url",
                "name": "name",
                "render": function (data, type, row, meta) {
                    return '<a href="' + data + '">' + row.name + '</a>';
                }
            },
            {
                "targets": 2,
                "className": "truncate",
                "createdRow": function(row){
                    var td = $(row).find(".truncate");
                    td.attr("title", td.html());
                }
            },
            {
                "targets": 1,
                "className": "truncatename",
                "createdRow": function(row){
                    var td = $(row).find(".truncate");
                    td.attr("title", td.html());
                }
            }
        ]
    });
    $('#myTable tbody').on('click', 'td.details-control', function () {
        var table = $('#myTable');
        var tr = $(this).closest('tr');
        var row = $('#myTable').DataTable().row( tr );

        if ( row.child.isShown() ) {
            // This row is already open - close it
            row.child.hide();
            tr.removeClass('shown');
        }
        else {
            // Open this row
            row.child( format(row.data()) ).show();
            tr.addClass('shown');
        }
    });
});