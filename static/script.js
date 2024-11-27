function buildTable(data) {
    var node = document.createElement("table");
    var tr = document.createElement("tr");
    var headers = Object.keys(data[0]);
    for (var i=0; i<headers.length; ++i) {
        var header = headers[i];
        var th = document.createElement("th");
        th.appendChild(document.createTextNode(header));
        tr.appendChild(th);
    }
    node.appendChild(tr);
    data.forEach(function (rowdata) {
       tr = document.createElement("tr");
       for (var i=0; i<headers.length; ++i) {
            var header = headers[i];
            var td = document.createElement("td");
            td.appendChild(document.createTextNode(rowdata[header]));
            if (typeof rowdata[header] == "number") {
                td.style.textAlign = "right";
                td.style.color = "#E50000";
            }
            tr.appendChild(td);
        }
        node.appendChild(tr);
    });
    return node;
}

var MOUNTAINS = [
{no: 0, name: "Kilimanjaro", height: 5895, country: "Tanzania"},
{no: 1, name: "Everest", height: 8848, country: "Nepal"},
{no: 2, name: "Mount Fuji", height: 3776, country: "Japan"},
{no: 3, name: "Mont Blanc", height: 4808, country: "Italy/France"},
{no: 4, name: "Vaalserberg", height: 323, country: "Netherlands"},
{no: 5, name: "Denali", height: 6168, country: "United States"},
{no: 6, name: "Popocatepetl", height: 5465, country: "Mexico"}
];
           
document.body.appendChild(buildTable(MOUNTAINS));


//take from codepen 

