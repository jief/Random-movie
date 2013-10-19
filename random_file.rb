#!/usr/bin/ruby

filelist = File.join("/mnt/movies", "**", "*.*")
puts filepath = Dir.glob(filelist).sample.gsub(/[\s()\[\]'"]/) { '\\'+$& }
exec("xdg-open #{filepath}")