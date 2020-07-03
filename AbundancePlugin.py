import sys

class AbundancePlugin:
   def input(self, filename):
      filestuff = open(filename, 'r')
      firstline = filestuff.readline().strip() # Read first line
      self.taxa = firstline.split(',')
      self.taxa.remove(self.taxa[0])  # Remove placeholder

      # Possibly remove quotes
      for i in range(len(self.taxa)):
         if self.taxa[i][0] == '\"':
            self.taxa[i] = self.taxa[i][1:len(self.taxa[i])-1]

      self.lines = []
      for line in filestuff:
         self.lines.append(line)

      self.sums = dict()
      for taxon in self.taxa:
         self.sums[taxon] = 0

   def run(self):
      self.tuples = []
      for line in self.lines:
         elements = line.split(',')
         elements.remove(elements[0]) # remove sample name
         for i in range(0, len(elements)):
            self.sums[self.taxa[i]] += float(elements[i])
      for key in self.sums:
         self.sums[key] /= len(self.lines)
         #if (self.sums[key] != 0):
         self.tuples.append((self.sums[key], key))
      self.tuples.sort()
      self.tuples.reverse()

   def output(self,filename):
      outstuff = open(filename, 'w')
      outstuff.write("Name\tAbundance\t\n");
      for mytuple in self.tuples:
         outstuff.write(mytuple[1]+"\t"+str(mytuple[0])+"\n")

