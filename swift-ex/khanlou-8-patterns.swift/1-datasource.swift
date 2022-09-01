class SKSectionedDataSource: NSObject {
    var sectionedObjects: [[AnyObject]] = []

    init(objects: [AnyObject], sectioningKey: String) {
        super.init()
        sectionObjects(objects, withKey: sectioningKey)
    }

    func sectionObjects(objects: [AnyObject], withKey sectioningKey: String) {
        //section the objects array
    }

    func numberOfSections() -> Int {
        return sectionedObjects.count
    }

    func numberOfObjectsInSection(section: Int) -> Int {
        return sectionedObjects[section].count
    }

    func objectAtIndexPath(indexPath: NSIndexPath) -> AnyObject {
        return sectionedObjects[indexPath.section][indexPath.row]
    }
}