This repo is to create a thin EPUB book for the [leet-code](https://github.com/youngyangyang04/leetcode-master), so that we can use calibre to maintain the e-book and send to Kindle.

If you want to generate the original e-book from the whole data of the [leet-code](https://github.com/youngyangyang04/leetcode-master). You can run the below pandoc command:

```bash
pandoc -o leet-code-full.epub --verbose --metadata-file=./title.txt --toc=true --toc-depth=1 --highlight-style=monochrome **/*.md
```

For installing the pandoc, please refer https://pandoc.org/installing.html.

```bash
--verbose            show the log for debugging
--metadata-file      metadata for the ebook
--toc                generate the table of contents
--toc-depth          define the depth of the toc
--highlight-style    hightlight the code style
```

If you want to generate the thin version of the [leet-code](https://github.com/youngyangyang04/leetcode-master), please follow below guideline:

1. Remove the unnecessary code block. Please note that the CPP code clock is hard to remove due to the book mainly use CPP to solve the problems.

```python
	python3 filter_code_block.py problems problems_out "python,Go,javascript,typescript,swift,csharp,c,scala,ruby,cs,js,kotlin,cangjie,ts,php,dart"
```

As I mainly focus on the java and Rust learning, so I remove others from java and Rust. You could set the removal variable accordingly.

2. Optional - Download all PNG to local folder and convert the linkage to local.

```bash
     sh convert-media.sh
```
   
   The convert-media.sh would convert all the MD files even in the sub-folder and download all the images in the "media" folder.

3. Run the pandoc command and send the epub book to Kindle via Calibre.

```bash
	 pandoc -o leet-code-thin.epub --verbose --metadata-file=./title.txt --toc=true --toc-depth=1 --highlight-style=monochrome **/*.md
```

