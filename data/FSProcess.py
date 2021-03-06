import csv

outfile = open('FS.czml','w')
outfile.write('[\n')
outfile.write('\t{\n')
outfile.write('\t\t"id": "document",\n')
outfile.write('\t\t"name": "The Globe of World Football",\n')
outfile.write('\t\t"version": "1.0"\n')
outfile.write('\t}')
with open('FootballStadiums.csv', 'rb') as csvfile:
	lineread = csv.reader(csvfile, delimiter=',')
	for row in lineread:
		outfile.write(',{\n')
		outfile.write('\t\t"id": "'+row[0]+'",\n')
		outfile.write('\t\t"name": "'+row[1]+'",\n')
		outfile.write('\t\t"description": "<table>')
		outfile.write('<tr><td>Team Name</td><td>'+row[1]+'</td></tr>')
		outfile.write('<tr><td>City</td><td>'+row[2]+'</td></tr>')
		outfile.write('<tr><td>Country</td><td>'+row[3]+'</td></tr>')
		outfile.write('<tr><td>League</td><td>'+row[4]+'</td></tr>')
		outfile.write('<tr><td>Stadium Name</td><td>'+row[5]+'</td></tr>')
		outfile.write('<tr><td>Stadium Capacity</td><td>'+row[6]+'</td></tr>')
		outfile.write('</table>",\n')
		outfile.write('\t\t"billboard": {\n')
		outfile.write('\t\t\t"image" : { "uri" : "./Soccer_Icon_Small.png" }\n')
		outfile.write('\t\t},\n')
		outfile.write('\t\t"position": {\n')
		outfile.write('\t\t\t"cartographicDegrees": ['+row[8]+','+row[7]+',0]\n')
		outfile.write('\t\t}\n')
		outfile.write('\t}')
outfile.write('\n]')
outfile.close()