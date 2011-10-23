import datetime
import aggregator.aggregate
import aggregator.generatewordindex 
import aggregator.generatekrantweight
import aggregator.generatecalculatedweight
import aggregator.generatecloudweight
import aggregator.generateranking

def main() :
#  while True :
    print 'start run_all.py'
    print datetime.datetime.now()
    print 'start aggregate'
    aggregator.aggregate.main()
    print datetime.datetime.now()
    print 'start generatewordindex'
    aggregator.generatewordindex.main()
    print datetime.datetime.now()
    print 'start generatekrantweight'
    aggregator.generatekrantweight.main()
    print datetime.datetime.now()
    print 'start generatecalculatedweight'
    aggregator.generatecalculatedweight.main()
    print datetime.datetime.now()
    print 'start generatecloudweight'
    aggregator.generatecloudweight.main()
    print datetime.datetime.now()
    print 'start generateranking'
    aggregator.generateranking.main()
    print datetime.datetime.now()
    print 'end run_all.py'

if __name__=='__main__':
#    Task.run_all()
    main()
