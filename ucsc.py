def main():
	with open('info.txt') as f:
		header = f.readline()
		for line in f:
			split_line = line.strip().split('\t')
			roi_transcript = split_line[0]
			roi_chrom = split_line[1]
			roi_gene = split_line[7]
			roi_starts = split_line[5].split(',')[:-1]
			roi_ends = split_line[6].split(',')[:-1]
			roi_exon_count = int(split_line[4])
			rois = zip(roi_starts,roi_ends)
			for num, roi in enumerate(rois):
				print '{} exon {}'.format(roi_gene, num + 1), int(roi[1]) - int(roi[0])


if __name__ == '__main__':
	main()