#!/usr/bin/perl
use strict;
use warnings;

#using bignum
my $Tindex = 0;
my @As     = (rand(), rand(), rand(), rand());
my @Cs     = (rand(), rand(), rand(), rand());

my @AZ = (
    rand(), rand(), rand(), rand(), rand(), rand(), rand(), rand(),
    rand(), rand(), rand(), rand(), rand(), rand(), rand(), rand()
);
my @CZ = (
    rand(), rand(), rand(), rand(), rand(), rand(), rand(), rand(),
    rand(), rand(), rand(), rand(), rand(), rand(), rand(), rand()
);

my @A = ('Ag0', 'Ag1', 'Ag2', 'Ag3', 'Ae4', 'Ae5', 'Ae6', 'Ae7');
my @B = ('G0', 'G1', 'G2', 'G3', 'E4', 'E5', 'E6', 'E7');

print " DIMMENSION \n";
print scalar(@A);
print " DIMMENSION \n";
print scalar(@B);

my @cay1 = cayley(\@A, \@B);
print "Hello World \n";
print "hello." . "\n";

print join(", ", @cay1);
print "\n".$Tindex;

# my @C = ('C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7');
# my @cay2 = cayley(\@C, \@cay1);
# print "Hello World \n";
# print "hello." . "\n";
# print join(", ", @cay2);
# print "\n".$Tindex;

my $length = scalar(@cay1);
my $index;
my $str;
my @spl;
my @spl1;
my $find;
my $replace;
for $index (0 .. $length - 1) {
    print "$index \n";
$str  = $cay1[$index];
# Here character is comma(, )
# using split() function
@spl = split(/[+-]/, $str);
# displaying result using foreach loop
my $strx="";
my $stry="";
my $strz="";
foreach my $i (@spl) 
{
    @spl1 = split(/[*]/, $i);
    $strz = join("*", sort(@spl1));
    $find = "m";
    $replace = "-";
    $strz=~ s/$find/$replace/;
    $find = "p";
    $replace = "+";
    $strz=~ s/$find/$replace/;
    $strx =$strx.$strz;
}
print ("", $strx);
    print "\n";
}

# my $length = scalar(@cay2);
# my $index;
# my $str;
# my @spl;
# for $index (0 .. $length - 1) {
#     print "$index \n";
# $str  = $cay2[$index];
# # Here character is comma(, )
# # using split() function
# @spl = split(/[+-]/, $str);
# # displaying result using foreach loop
# foreach my $i (@spl) 
# {
#     print "$i \n";
# }
# }




sub cayley {
    my ($ref1, $ref2) = @_;
    my @input1 = @{$ref1};
    my @input2 = @{$ref2};

    #print join(", ", @input1);
    #print " \n";
    #print join(", ", @input2);
    my $order1 = scalar(@input1);
    my $order2 = scalar(@input2);
    my @output;
    if ($order1 != $order2) {
        die;
    }
    if ($order1 == 1) {
        $output[0] = $input1[0]."*".$input2[0];
    } else {
        $Tindex = $Tindex + 1;
        my @A       = @input1[ 0 .. $order1 / 2 - 1 ];
        my @B       = @input1[ $order1 / 2 .. $order1 - 1 ];
        my @C       = @input2[ 0 .. $order1 / 2 - 1 ];
        my @D       = @input2[ $order1 / 2 .. $order1 - 1 ];
        my $lengthZ = scalar(@D);
        my @conjD;
        my @conjC;
        my $indexZ;

        for $indexZ (0 .. $lengthZ - 1) {
            if ($indexZ == 0) {
                $conjC[$indexZ] = 'yy' . $Tindex . '*' . $C[$indexZ];
                $conjD[$indexZ] = 'yy' . $Tindex . '*' . $D[$indexZ];
            } else {
                $conjC[$indexZ] = 'xx' . $Tindex . '*' . $C[$indexZ];
                $conjD[$indexZ] = 'xx' . $Tindex . '*' . $D[$indexZ];
            }
        }
        my @cay1 = cayley(\@A,     \@C);
        my @cay2 = cayley(\@conjD, \@B);
        my @cay3 = cayley(\@D,     \@A);
        my @cay4 = cayley(\@B,     \@conjC);
        my @left;
        my @right;
        my $length = scalar(@cay1);
        my $index;

        for $index (0 .. $length - 1) {
            $left[$index]  = $cay1[$index] . '-m-' . $cay2[$index];
            $right[$index] = $cay3[$index] . '+p+' . $cay4[$index];
        }
        @output = (@left, @right);
    }
    return @output;
}