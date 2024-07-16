******************************************
PointCloudReduce & SubsetPointCloud
******************************************



ReducePointCloud
----------------

.. image:: ../images/Pointcloud/Pointcloudreduce.png

.. topic:: Definition

  Reduces the number of points in a Point Cloud by a given fraction.


**Input**

.. table::
  :align: left
    
  =========== ======================================  ==============
  Name        Description                             Type
  =========== ======================================  ==============
  Point Cloud Point Cloud to Reduce                   Point Cloud
  Fraction    Fraction of Points to remain            Number
  =========== ======================================  ==============

**Output**

.. table::
  :align: left
    
  ===========  ======================================  ==============
  Name         Description                              Type
  ===========  ======================================  ==============
  Point Cloud  Reduced Point Cloud                      Point Cloud
  ===========  ======================================  ==============




SubsetPointCloud
-----------------

.. image:: ../images/Pointcloud/Pointcloudbox.png

.. topic:: Definition

  Sections a Point Cloud by a selection box volume.


**Input**

.. table::
  :align: left

  =============   ======================================  ==============
  Name            Description                             Type
  =============   ======================================  ==============
  Point Cloud     Point Cloud to Reduce                   Point Cloud
  Selection box   Volume you want to keep                 Box
  =============   ======================================  ==============

**Output**

.. table::
  :align: left
    
  ===========  ======================================  ==============
  Name         Description                             Type
  ===========  ======================================  ==============
  Point Cloud  Selection of Point Cloud                Point Cloud
  ===========  ======================================  ==============