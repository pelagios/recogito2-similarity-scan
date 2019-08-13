require 'pg'
require 'jaro_winkler'

# Pull all document records from the DB
conn = PG.connect('localhost', 5432, '', '', 'recogito-test', 'postgres', 'postgres')

sql = 'SELECT author, title, owner, date_numeric FROM document'
records = conn.exec(sql).select { |r| r['title'] != 'Welcome to Recogito' }

puts "Computing distances for #{records.size} records"

start = Time.now

# Run any-to-any Jaro-Winkler comparison
ctr = 0
records.each do |this_row|
  records.each do |that_row|
    if this_row != that_row
      a = this_row['title']
      a_owner = this_row['owner']
    
      b = that_row['title']
      b_owner = that_row['owner']

      ctr++
      dist = JaroWinkler.distance(a, b)

      if dist > 0.92 && a_owner != b_owner && !a.downcase.include?("test")
        puts "#{a}/#{a_owner} to #{b}/#{b_owner}: #{dist}"
      end
    end
  end
end

puts "Ran #{ctr} comparisons"
puts "Done. Took #{Time.now - start}s"


