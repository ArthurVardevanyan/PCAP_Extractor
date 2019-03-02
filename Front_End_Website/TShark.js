$(document).ready(function() {
    $('#Table1Data').DataTable( {
        responsive: {
            details: {
                renderer: function ( api, rowIdx, columns ) {
                    var data = $.map( columns, function ( col, i ) {
                        return col.hidden ?
                            '<tr data-dt-row="'+col.rowIndex+'" data-dt-column="'+col.columnIndex+'">'+
                                '<td>'+col.title+':'+'</td> '+
                                '<td>'+col.data+'</td>'+
                            '</tr>' :
                            '';
                    } ).join('');
 
                    return data ?
                        $('<table/>').append( data ) :
                        false;
                }
            }
        },
        //scrollX: true,
        columnDefs: [
            {

           	targets: [1,2,3,4],
                render: $.fn.dataTable.render.number(',', '.', 0, '')           

            },
            
                { "width": "20%", "targets": 7},
           
        ],

    } );
} );
$(document).ready(function() {
    $('#Table2Data').DataTable( {
        responsive: {
            details: {
                renderer: function ( api, rowIdx, columns ) {
                    var data = $.map( columns, function ( col, i ) {
                        return col.hidden ?
                            '<tr data-dt-row="'+col.rowIndex+'" data-dt-column="'+col.columnIndex+'">'+
                                '<td>'+col.title+':'+'</td> '+
                                '<td>'+col.data+'</td>'+
                            '</tr>' :
                            '';
                    } ).join('');
 
                    return data ?
                        $('<table/>').append( data ) :
                        false;
                }
            }
        },
        //scrollX: true,
        columnDefs: [
            {

           	targets: [2,3,4,5],
                render: $.fn.dataTable.render.number(',', '.', 0, '')           
            },
        ]
    } );
} );
